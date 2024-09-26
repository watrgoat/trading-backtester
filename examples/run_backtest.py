# examples/run_backtest.py
from src.data_handler import DataHandler
from src.portfolio import Portfolio
from src.execution_handler import ExecutionHandler
from src.logger import Logger
from src.backtester import Backtester
from src.performance import Performance
from src.visualizer import Visualizer
from my_strategy import MovingAverageStrategy
import pandas as pd

# Initialize components
data_handler = DataHandler(ticker='AAPL', start_date='2020-01-01', end_date='2023-01-01')
strategy = MovingAverageStrategy()
portfolio = Portfolio(initial_capital=100000)
execution_handler = ExecutionHandler(transaction_cost=0.001)
logger = Logger()

# Initialize backtester
backtester = Backtester(data_handler, strategy, portfolio, execution_handler, logger)

# Run backtest
portfolio_values, trades = backtester.run_backtest()

# Calculate performance
returns = pd.Series(portfolio_values).pct_change().dropna()
total_return = Performance.calculate_total_return(portfolio_values)
sharpe_ratio = Performance.calculate_sharpe_ratio(returns)
max_drawdown = Performance.calculate_max_drawdown(portfolio_values)

# Print performance
print(f"Total Return: {total_return:.2%}")
print(f"Sharpe Ratio: {sharpe_ratio:.2f}")
print(f"Max Drawdown: {max_drawdown:.2%}")

# Visualize results
visualizer = Visualizer()
visualizer.plot_equity_curve(data_handler.data.index, portfolio_values)
visualizer.plot_trades(data_handler.data, trades)
