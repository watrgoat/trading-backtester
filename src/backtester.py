
class Backtester:
    def __init__(self, data_handler, strategy, portfolio, execution_handler, logger):
        """
        Initializes the backtester with necessary components.
        
        Parameters:
        - data_handler: The data handler instance that provides historical data.
        - strategy: The trading strategy to generate buy/sell signals.
        - portfolio: The portfolio instance to track positions and cash.
        - execution_handler: The execution handler responsible for executing trades.
        - logger: The logger instance to log trades and events.
        """
        self.data_handler = data_handler
        self.strategy = strategy
        self.portfolio = portfolio
        self.execution_handler = execution_handler
        self.logger = logger
        self.trades = []  # List to store executed trades

    def run_backtest(self):
        """
        Runs the backtest by generating signals, executing trades, and updating the portfolio.
        
        Returns:
        - A list of portfolio values over time and a list of trades executed during the backtest.
        """
        data = self.data_handler.get_data()  # Load historical data for all tickers
        signals = self.strategy.generate_signals(data)  # Generate buy/sell signals

        for current_date, signal in signals.items():
            for ticker in self.data_handler.tickers:  # Iterate over multiple tickers if needed
                current_price = data.loc[current_date]['Close'] if len(self.data_handler.tickers) == 1 else data.loc[current_date, ticker]['Close']
                
                if signal == 1:  # Buy signal
                    order = {
                        'symbol': ticker,
                        'type': 'buy',
                        'quantity': 10,
                        'price': current_price,
                        'date': current_date  # Ensure the date is included in the order
                    }
                    trade = self.execution_handler.execute_order(order)
                    self.portfolio.update_holdings(trade)
                    self.trades.append(trade)
                    self.logger.log_event(f"BUY {trade['quantity']} {trade['symbol']} at {trade['price']} on {trade['date']}")
                
                elif signal == -1:  # Sell signal
                    order = {
                        'symbol': ticker,
                        'type': 'sell',
                        'quantity': 10,
                        'price': current_price,
                        'date': current_date  # Ensure the date is included in the order
                    }
                    trade = self.execution_handler.execute_order(order)
                    self.portfolio.update_holdings(trade)
                    self.trades.append(trade)
                    self.logger.log_event(f"SELL {trade['quantity']} {trade['symbol']} at {trade['price']} on {trade['date']}")

                # Update portfolio value on every date for each ticker
                self.portfolio.calculate_portfolio_value({ticker: current_price})

        return self.portfolio.get_portfolio_values(), self.trades
