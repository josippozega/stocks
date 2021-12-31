import yfinance as yf
import streamlit as st

st.write("""
# Jednostavna aplikacija za cijenu dionica
Prikazane su zaključna cijena dionica i količina Googlea!
""")


#define the ticker symbol
tickerSymbol = 'GOOGL'
tickerSymbol2 = 'AAPL'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
tickerData2 = yf.Ticker(tickerSymbol2)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
tickerDf2 = tickerData2.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)

st.write("""
# Jednostavna aplikacija za cijenu dionica
Prikazane su zaključna cijena dionica i količina Applea!
""")

st.line_chart(tickerDf2.Close)
st.line_chart(tickerDf2.Volume)
