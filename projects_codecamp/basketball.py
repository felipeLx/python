import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import base64
import pandas as pd
import numpy as np

st.title('Basktball Players')
st.markdown('NBA Players Stats')

st.sidebar.header('User input features')
selected_year = st.sidebar.selectbox('Year', list(reversed(range(1950, 2021))))

# web scraping NBA players stats
@st.cache
def load_data(year):
    url = "https://www.basketball-reference.com/leagues/NBA_" + str(year) + "_per_game.html"
    html = pd.read_html(url, header=0)
    df = html[0]
    raw = df.drop(df[df['Age'] == 'Age'].index)
    raw = raw.fillna(0)
    playerstats = raw.drop(['Rk', '3P%', '2P%', 'eFG%', 'FT%', 'FG%'], axis = 1)
    return playerstats

playerstats = load_data(selected_year)

# team selection
sorted_unique_team = sorted(playerstats['Tm'].unique())
selected_team = st.sidebar.multiselect('Team', sorted_unique_team)

# position selection
unique_pos = ['C', 'PF', 'SF', 'SG', 'PG']
selected_pos = st.sidebar.multiselect('Position', unique_pos, default = unique_pos)

# filtering data
df_selected_team = playerstats[(playerstats['Tm'].isin(selected_team)) & (playerstats['Pos'].isin(selected_pos))]

st.header('Display player stats from selected team(s)')
st.write('Data Dimension: ' + str(df_selected_team.shape[0]) + ' rows and ' + str(df_selected_team.shape[1]) + ' columns')

st.dataframe(df_selected_team)

# download NBA players stats
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode() # string to bytes
    href = f'<a href="data:file/csv;base64,{b64}" download="playerstats.csv">Download csv file</a>'
    return href

st.markdown(filedownload(df_selected_team), unsafe_allow_html=True)

# chart building
if st.button('Heatmap'):
    st.header('Matrix Heatmap')
    df_selected_team.to_csv('output.csv', index=False)
    df = pd.read_csv('output.csv')

    correlation = df.corr()
    mask = np.zeros_like(correlation)
    mask[np.triu_indices_from(mask)] = True
    with sns.axes_style("white"):
        fig, ax = plt.subplots(figsize=(10, 10))
        ax = sns.heatmap(correlation, mask=mask, vmax=1, square=True)
    st.pyplot(fig)