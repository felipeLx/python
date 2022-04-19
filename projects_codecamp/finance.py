import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Stock price tracker
""")

tickerSymbol = st.text_input("Enter ticker symbol: ", max_chars=5, placeholder="AAPL")
startDate = st.text_input("Enter start date (YYYY-MM-DD): ")
endDate = st.text_input("Enter end date (YYYY-MM-DD): ")
period_range = st.text_input("Enter period range (1m, 1d, 1wk, 1mo): ", placeholder="1d")

if len(tickerSymbol) > 0 & len(startDate) > 0 & len(endDate) > 0 & len(period_range) > 0:
    tickerData = yf.Ticker(tickerSymbol)
    tickerOf = tickerData.history(period=period_range, start=startDate, end=endDate)
    st.line_chart(tickerOf.Close)
    st.line_chart(tickerOf.Volume)


