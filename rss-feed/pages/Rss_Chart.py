import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Market Chart", page_icon="📈")
st.markdown("# Gráfico das empresas SA do rss-feed")
st.sidebar.markdown("# Gráfico do Mercado 📈")

def read_dataframe():
    df_load = pd.read_csv('./data/rss.csv', dtype=str, index_col=0)
    df_business = df_load[['Org','Symbol']].reset_index(drop=True)
    df_business['name'] = df_business['Org'].str.lower()
    df_business['name'] = df_business['name'].str.split( ).str[0]
    df_business['code'] = df_business['Symbol'].str[0:5] + '.SA'
    df_business['info_col'] = df_business['name'] + '-' + df_business['code']
    return df_business

def extracting_table_generate_plot(page_name):
    url = "https://br.financas.yahoo.com/quote/" + page_name + "/history?p=" + page_name + "&.tsrc=fin-srch"
    r_client = requests.get(url, headers={'User-Agent': 'Custom'})
   
    try:
        soup_client = BeautifulSoup(r_client.content, 'html.parser')
        table_client = soup_client.find('table', attrs={'data-test': 'historical-prices', 'class': 'W(100%) M(0)'})
        df = pd.read_html(str(table_client), decimal=',', thousands='.')[0]
        
        # cut the data frame to manipulate manually the month
        df = df.iloc[0:30]
        
        # clean and transform the dataframe
        df = df[['Data', 'Fechamento*']]
        df['Data'] = df['Data'].str.replace(' de ', '/')
        df = df[~df['Fechamento*'].str.contains('Dividendo')]
        df['Data'] = df['Data'].str.replace('jun.', '06')
        df['Data'] = df['Data'].str.replace('mai.', '05')
        df['Data'] = df['Data'].str.replace('abr.', '04')
        df['Data'] = pd.to_datetime(df['Data'], format="%d/%m/%Y")
        df['Fechamento*'] = pd.to_numeric(df['Fechamento*'], downcast='float')
        df['Fechamento*'] = df['Fechamento*'].round(2)

        fig = plt.figure(figsize=(10, 4))
        sns.lineplot(x='Data', y="Fechamento*", data=df, color='#0066ff')
        plt.title(page_name)
        st.pyplot(fig)
        with st.expander('Expandir para ver os dados'):
            st.dataframe(df)
        
    except:
          return st.write('Não foi possível gerar o gráfico com o código ' + page_name)
          # return st.write('Página não encontrada: ' + str(r_client.status_code) + ' - Page ' + r_client.reason)

page_names_to_funcs = read_dataframe()
asset_selected = st.sidebar.selectbox("Selecionar o Ativo", set(list(page_names_to_funcs['code'])))
page_name = page_names_to_funcs['code'].loc[page_names_to_funcs['code'] == asset_selected].values[0]

extracting_table_generate_plot(page_name)
