# src/performance.py
import numpy as np

class Performance:
    @staticmethod
    def calculate_total_return(portfolio_values):
        return (portfolio_values[-1] / portfolio_values[0]) - 1
    
    @staticmethod
    def calculate_sharpe_ratio(returns, risk_free_rate=0.0):
        excess_returns = returns - risk_free_rate
        return np.mean(excess_returns) / np.std(excess_returns) * np.sqrt(252)
    
    @staticmethod
    def calculate_max_drawdown(portfolio_values):
        cum_max = np.maximum.accumulate(portfolio_values)
        drawdowns = (cum_max - portfolio_values) / cum_max
        return np.max(drawdowns)