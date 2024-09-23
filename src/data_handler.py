# src/data_handler.py
import pandas as pd
import yfinance as yf

class DataHandler:
    def __init__(self, ticker, start_date, end_date):
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date
        self.data = self.load_data()
    
    def load_data(self):
        data = yf.download(self.ticker, start=self.start_date, end=self.end_date)
        data.dropna(inplace=True)
        return data
    
    def get_data(self):
        return self.data