import streamlit as st
import pandas as pd
import yfinance as yf
from GoogleNews import GoogleNews


def prices(ticker, START_DATE, END_DATE):
    stock = yf.Ticker(ticker)

    #Retrieve dataframe of stock prices in given timeframe
    hist = stock.history(start=START_DATE, end=END_DATE)
    hist = hist.reset_index()
    for i in ['Open', 'High', 'Close', 'Low']: 

        hist[i]  =  hist[i].astype('float64')
    st.write('Price Movement for ', ticker)

    #Display time series plot
    st.line_chart(data=hist, x="Date", y="Open")

def news(ticker, START_DATE, END_DATE):
    
    #Adjust date
    START_DATE = START_DATE.replace("-", "/")
    END_DATE = START_DATE.replace("-", "/")

    START_DATE = START_DATE[5:len(START_DATE)] + "/" + START_DATE[0:4]
    END_DATE = END_DATE[5:len(END_DATE)] + "/" + END_DATE[0:4]
   

    #Retrieve news headlines of stock in given timeframe
    news=GoogleNews(start=START_DATE,end=END_DATE)
    news.search(ticker)
    result=news.result()

    #Create dataframe of news heading, source, link
    df=pd.DataFrame(result)

    #Display dataframe
    st.write(df)


def main():
    st.title('Stock Info App')
    st.subheader("Enter Parameters")
    with st.form(key='form1'):
        #Display parameters
        ticker = st.text_input("Stock (Enter Ticker Symbol)")
        START_DATE = st.text_input("Enter Start Date:")
        END_DATE = st.text_input("Enter End Date:")
        submit_button = st.form_submit_button(label = "Retrieve Stock Info")
    if submit_button:
        #Retrieve and display Price movements and news headlines
        prices(ticker, START_DATE, END_DATE)
        news(ticker, START_DATE, END_DATE)



if __name__ == '__main__':
    main()



