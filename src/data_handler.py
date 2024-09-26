import pandas as pd
import yfinance as yf

class DataHandler:
    def __init__(self, tickers, start_date, end_date, source='yfinance'):
        """
        Initializes the data handler for fetching historical price data.

        Parameters:
        - tickers (str or list): The stock ticker symbol(s) to retrieve (e.g., 'AAPL' or ['AAPL', 'GOOG']).
        - start_date (str): The start date for the historical data in 'YYYY-MM-DD' format.
        - end_date (str): The end date for the historical data in 'YYYY-MM-DD' format.
        - source (str): The data source to use for fetching historical data (default is 'yfinance').
        """
        if isinstance(tickers, str):
            self.tickers = [tickers]  # Always handle tickers as a list for flexibility
        else:
            self.tickers = tickers
        self.start_date = start_date
        self.end_date = end_date
        self.source = source
        self.data = self.load_data()
    
    def load_data(self):
        """
        Fetches historical price data for the provided tickers from the chosen data source.
        
        Currently supports yfinance as the data source. Can be extended to other sources.
        
        Returns:
        - pd.DataFrame: A dataframe containing the historical price data for the specified tickers.
        """
        if self.source == 'yfinance':
            data = yf.download(self.tickers, start=self.start_date, end=self.end_date)
        else:
            raise ValueError(f"Data source '{self.source}' is not supported.")
        
        # Handle missing data by dropping NaN values
        data.dropna(inplace=True)
        
        # If handling multiple tickers, make sure the data is properly structured
        if len(self.tickers) > 1:
            data = data.stack(level=0).rename_axis(['Date', 'Ticker']).reset_index(level=1)
        
        return data

    def get_data(self):
        """
        Returns the historical price data.

        Returns:
        - pd.DataFrame: The previously loaded historical data.
        """
        return self.data

    def get_latest_price(self, symbol):
        """
        Get the most recent closing price for a specific symbol.
        
        Parameters:
        - symbol (str): The ticker symbol to get the latest price for.
        
        Returns:
        - float: The most recent closing price of the given symbol.
        """
        if symbol not in self.tickers:
            raise ValueError(f"Symbol '{symbol}' is not available in the data.")
        
        return self.data[self.data['Ticker'] == symbol]['Close'].iloc[-1]

    def get_prices_for_date(self, date):
        """
        Get the closing prices for all tickers on a specific date.
        
        Parameters:
        - date (str): The date in 'YYYY-MM-DD' format for which prices are requested.
        
        Returns:
        - pd.Series: A series of closing prices indexed by ticker symbol for the given date.
        """
        try:
            return self.data.loc[date, 'Close']
        except KeyError:
            raise ValueError(f"No data available for the date '{date}'")
