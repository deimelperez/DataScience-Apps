import numpy as np
import pandas as pd
import yfinance as yf
import streamlit as st


st.write("""
# Simple stock price

Shown are stocks prices and volume
""")


tickerSymbol = 'GOOGL'
tickerData = yf.Ticker(tickerSymbol)
tickerDF = tickerData.history(
    period='1d', start='2010-05-01', end='2021-02-01')


st.write('''
### Close price
''')
st.line_chart(tickerDF.Close)
st.write('''
### Volume
''')
st.line_chart(tickerDF.Volume)
