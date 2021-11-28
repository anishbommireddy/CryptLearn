import streamlit as st
import yfinance as yf
import pandas as pd
import cufflinks as cf
import datetime
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

#App title
st.markdown('''
# Stock Price App
Shown are the stock price data for query companies
- Built in 'Python' using 'streamlit', 'yfinance', 'cufflinks', 'pandas', and 'datetime'
''')
st.write('---')

#Sidebar
st.sidebar.subheader('Query parameters')
start_date = st.sidebar.date_input("Start date", datetime.date(2019, 1, 1))
end_date = st.sidebar.date_input("End date", datetime.date(2021, 1, 31))

#Retrieving tickers data
ticker_list = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/s-and-p-500-companies/master/data/constituents_symbols.txt')
tickerSymbol = st.sidebar.selectbox('Stock ticker', ticker_list)
tickerData = yf.Ticker(tickerSymbol) #get ticker Data
tickerDf = tickerData.history(period='1d', start=start_date, end=end_date) #get data

#Ticker Information
#string_logo = '<img src=%s>' % tickerData.info['logo url']
#st.markdown(string_logo, unsafe_allow_html=True)

string_name = tickerData.info['longName']
st.header('**%s**' % string_name)

string_summary = tickerData.info['longBusinessSummary']
st.info(string_summary)

#Ticker Data
st.header('**Ticker Data**')
st.write(tickerDf)

#Bollinger bands
st.header('**Bollinger Bands**')
qf=cf.QuantFig(tickerDf, title='First Quant Figure', legend='top',name='GS')
qf.add_bollinger_bands()
fig = qf.iplot(asFigure=True)
st.plotly_chart(fig)



###
#st.write('---')
#st.write(tickerData.info)
