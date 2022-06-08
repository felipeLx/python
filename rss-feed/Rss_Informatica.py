import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Market Chart", page_icon="📈")
st.markdown("# Chart for Business mentionate on the rss-feed")
st.sidebar.markdown("# Market Chart 📈")