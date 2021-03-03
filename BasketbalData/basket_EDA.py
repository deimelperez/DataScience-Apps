import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import base64

st.title('NBA Players Stats Explorer')

st.write("""
This app performs simple webscraping of NBA player stats data!

""")

st.sidebar.header('User Input Features')
selecte_year = st.sidebar.selectbox('Year', list(reversed(range(1950, 2022))))

# Web scraping


@st.cache
def load_data(year):
    url = 'https://www.basketball-reference.com/leagues/NBA_' + \
        str(year) + '_per_game.html'
    html = pd.read_html(url, header=0)
    df = html[0]
    df
    # Deletes repeating headers in content
    raw = df.drop(df[df.Age == 'Age'].index)
    raw = raw.fillna(0)
    playerStats = raw.drop(['Rk'], axis=1)
    return playerStats


playerStats = load_data(selecte_year)
playerStats
