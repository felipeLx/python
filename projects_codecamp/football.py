import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.title('NFL Football Stats')
st.markdown('NFL Players Stats')

st.sidebar.header('User input features')
selected_year = st.sidebar.selectbox('Year', list(reversed(range(2000, 2021))))

@st.cache
def load_data(year):
    url = 'https://www.pro-football-reference.com/years/' + str(year) + '/rushing.htm'
    html = pd.read_html(url, header=1)
    df = html[0]
    print(df.columns)
    raw = df.drop(df[df.Age == 'Age'].index)
    raw = raw.fillna(0)
    playerstats = raw.drop('Rk', axis = 1)
    return playerstats

playerstats = load_data(selected_year)

# team selection
sorted_unique_team = sorted(playerstats['Tm'].unique())
selected_team = st.sidebar.multiselect('Team', sorted_unique_team, sorted_unique_team)

# position selection
unique_pos = ['RB', 'WR', 'TE', 'QB', 'K', 'DEF']
selected_pos = st.sidebar.multiselect('Position', unique_pos, unique_pos)

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

# heatmap
if st.button('Heatmap'):
    st.header('Matrix Heatmap')
    df_selected_team.to_csv('output.csv', index=False)
    df = pd.read_csv('output.csv')
    
    correlation = df.corr()
    mask = np.zeros_like(correlation)
    mask[np.triu_indices_from(mask)] = True
    with sns.axes_style("white"):
        fig, ax = plt.subplots(figsize=(10, 10))
        ax = sns.heatmap(correlation, mask=mask, vmax=1, square=True, fmt='.2f', cmap='coolwarm')
    st.pyplot(fig)