# src/backtester.py
class Backtester:
    def __init__(self, data_handler, strategy, portfolio, execution_handler, logger):
        self.data_handler = data_handler
        self.strategy = strategy
        self.portfolio = portfolio
        self.execution_handler = execution_handler
        self.logger = logger
        self.trades = []
    
    def run_backtest(self):
        data = self.data_handler.get_data()
        signals = self.strategy.generate_signals(data)
        
        for index, row in data.iterrows():
            current_data = data.loc[:index]
            signal = signals.loc[index]
            if signal == 1:  # Buy signal
                order = {'symbol': self.data_handler.ticker, 'type': 'buy', 'quantity': 10, 'price': row['Close']}
                trade = self.execution_handler.execute_order(order)
                self.portfolio.update_holdings(trade)
                self.trades.append(trade)
                self.logger.log_event(f"BUY {trade['quantity']} {trade['symbol']} at {trade['price']}")
            elif signal == -1:  # Sell signal
                order = {'symbol': self.data_handler.ticker, 'type': 'sell', 'quantity': 10, 'price': row['Close']}
                trade = self.execution_handler.execute_order(order)
                self.portfolio.update_holdings(trade)
                self.trades.append(trade)
                self.logger.log_event(f"SELL {trade['quantity']} {trade['symbol']} at {trade['price']}")
        
        return self.portfolio.get_portfolio_values(), self.trades