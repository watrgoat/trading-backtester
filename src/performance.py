import numpy as np

class Performance:
    @staticmethod
    def calculate_total_return(portfolio_values):
        """
        Calculate the total return of the portfolio.

        Parameters:
        - portfolio_values (list): List of portfolio values over time.

        Returns:
        - float: Total return as a percentage.
        """
        return (portfolio_values[-1] / portfolio_values[0]) - 1
    
    @staticmethod
    def calculate_annualized_return(portfolio_values, periods_per_year=252):
        """
        Calculate the annualized return of the portfolio.

        Parameters:
        - portfolio_values (list): List of portfolio values over time.
        - periods_per_year (int): Number of trading periods in a year (default is 252 for daily).

        Returns:
        - float: Annualized return as a percentage.
        """
        total_return = Performance.calculate_total_return(portfolio_values)
        num_periods = len(portfolio_values)
        return (1 + total_return) ** (periods_per_year / num_periods) - 1
    
    @staticmethod
    def calculate_sharpe_ratio(returns, risk_free_rate=0.0, periods_per_year=252):
        """
        Calculate the Sharpe ratio, which measures risk-adjusted return.

        Parameters:
        - returns (pd.Series or np.array): Periodic returns of the portfolio.
        - risk_free_rate (float): Risk-free rate of return (default is 0).
        - periods_per_year (int): Number of periods per year (default 252 for daily).

        Returns:
        - float: Sharpe ratio (higher is better).
        """
        excess_returns = returns - risk_free_rate / periods_per_year
        return np.mean(excess_returns) / np.std(excess_returns) * np.sqrt(periods_per_year)
    
    @staticmethod
    def calculate_sortino_ratio(returns, risk_free_rate=0.0, periods_per_year=252):
        """
        Calculate the Sortino ratio, which is similar to Sharpe but only considers downside risk.

        Parameters:
        - returns (pd.Series or np.array): Periodic returns of the portfolio.
        - risk_free_rate (float): Risk-free rate of return (default is 0).
        - periods_per_year (int): Number of periods per year (default 252 for daily).

        Returns:
        - float: Sortino ratio (higher is better).
        """
        excess_returns = returns - risk_free_rate / periods_per_year
        downside_risk = np.std([x for x in excess_returns if x < 0])
        return np.mean(excess_returns) / downside_risk * np.sqrt(periods_per_year)

    @staticmethod
    def calculate_max_drawdown(portfolio_values):
        """
        Calculate the maximum drawdown, which measures the largest peak-to-trough decline.

        Parameters:
        - portfolio_values (list): List of portfolio values over time.

        Returns:
        - float: Maximum drawdown as a percentage.
        """
        cum_max = np.maximum.accumulate(portfolio_values)
        drawdowns = (cum_max - portfolio_values) / cum_max
        return np.max(drawdowns)
    
    @staticmethod
    def calculate_volatility(returns, periods_per_year=252):
        """
        Calculate the annualized volatility of the portfolio.

        Parameters:
        - returns (pd.Series or np.array): Periodic returns of the portfolio.
        - periods_per_year (int): Number of periods per year (default 252 for daily).

        Returns:
        - float: Annualized volatility as a percentage.
        """
        return np.std(returns) * np.sqrt(periods_per_year)
