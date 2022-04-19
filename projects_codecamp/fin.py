import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Stock price tracker
""")

tickerSymbol = 'GOOGL'
tickerData = yf.Ticker(tickerSymbol)

tickerOf = tickerData.history(period='1d', start='2022-01-01', end='2022-01-01')

st.line_chart(tickerOf.Close)
st.line_chart(tickerOf.Volume)