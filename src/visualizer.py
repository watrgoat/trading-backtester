import matplotlib.pyplot as plt
import pandas as pd

class Visualizer:
    """
    A class for visualizing backtest results, including the equity curve
    and trade executions on price charts.
    """
    
    def __init__(self, style='ggplot'):
        """
        Initializes the Visualizer with a specific plot style.
        
        Parameters:
            style (str): The matplotlib style to use for plots.
        """
        plt.style.use(style)
    
    def plot_equity_curve(self, dates, portfolio_values):
        """
        Plots the equity curve of the portfolio over time.
        
        Parameters:
            dates (pd.DatetimeIndex or list): The dates corresponding to the portfolio values.
            portfolio_values (list or pd.Series): The portfolio value at each date.
        """
        plt.figure(figsize=(14, 7))
        plt.plot(dates, portfolio_values, label='Equity Curve', color='blue')
        plt.title('Portfolio Equity Curve')
        plt.xlabel('Date')
        plt.ylabel('Portfolio Value ($)')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    
    def plot_trades(self, data, trades):
        """
        Plots the stock's closing price and marks buy/sell trades.
        
        Parameters:
            data (pd.DataFrame): The historical price data with a DateTime index.
            trades (list of dict): A list of trade dictionaries with keys:
                                   - 'type': 'buy' or 'sell'
                                   - 'price': Execution price
                                   - 'date': Execution date (should be in data.index)
        """
        plt.figure(figsize=(14, 7))
        plt.plot(data.index, data['Close'], label='Close Price', color='black')
        
        # Separate buy and sell trades
        buys = [trade for trade in trades if trade['type'] == 'buy']
        sells = [trade for trade in trades if trade['type'] == 'sell']
        
        # Plot buy trades
        if buys:
            buy_dates = [trade['date'] for trade in buys]
            buy_prices = [trade['price'] for trade in buys]
            plt.scatter(buy_dates, buy_prices, marker='^', color='green', label='Buy', s=100, edgecolors='k')
        
        # Plot sell trades
        if sells:
            sell_dates = [trade['date'] for trade in sells]
            sell_prices = [trade['price'] for trade in sells]
            plt.scatter(sell_dates, sell_prices, marker='v', color='red', label='Sell', s=100, edgecolors='k')
        
        plt.title('Trades on Close Price Chart')
        plt.xlabel('Date')
        plt.ylabel('Price ($)')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()
