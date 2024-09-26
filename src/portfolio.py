
class Portfolio:
    def __init__(self, initial_capital: float, transaction_cost: float = 0.0):
        """
        Initialize the portfolio with starting capital and transaction costs.

        Parameters:
        - initial_capital (float): Starting amount of cash in the portfolio.
        - transaction_cost (float): Cost of executing a trade, as a percentage (e.g., 0.001 for 0.1% per trade).
        """
        self.initial_capital = initial_capital
        self.cash = initial_capital
        self.transaction_cost = transaction_cost
        self.positions = {}  # Current positions held (symbol -> quantity)
        self.trade_history = []  # Stores all trades made
        self.portfolio_values = []  # Tracks portfolio value over time

    def update_holdings(self, trade: dict):
        """
        Update the portfolio's holdings based on a trade.

        Parameters:
        - trade (dict): A dictionary representing the trade details. Example:
            {
                'symbol': 'AAPL',
                'type': 'buy' or 'sell',
                'quantity': 10,
                'price': 150.0,
                'date': '2023-01-01'
            }
        """
        symbol = trade['symbol']
        qty = trade['quantity']
        price = trade['price']
        trade_cost = qty * price * self.transaction_cost

        if trade['type'] == 'buy':
            # Decrease cash, account for transaction cost
            self.cash -= (qty * price) + trade_cost
            self.positions[symbol] = self.positions.get(symbol, 0) + qty

        elif trade['type'] == 'sell':
            # Increase cash, account for transaction cost
            self.cash += (qty * price) - trade_cost
            self.positions[symbol] = self.positions.get(symbol, 0) - qty

        # Record the trade in trade history
        self.trade_history.append({
            'symbol': symbol,
            'type': trade['type'],
            'quantity': qty,
            'price': price,
            'cost': trade_cost,
            'date': trade['date']
        })

    def calculate_portfolio_value(self, current_prices: dict):
        """
        Calculate the total portfolio value based on the current prices of held assets.

        Parameters:
        - current_prices (dict): A dictionary of the latest prices for each asset. Example:
            {
                'AAPL': 150.0,
                'GOOG': 2500.0
            }
        """
        total_value = self.cash  # Start with available cash
        for symbol, qty in self.positions.items():
            if qty > 0:  # Only calculate value for held positions
                total_value += qty * current_prices.get(symbol, 0)

        self.portfolio_values.append(total_value)

    def get_portfolio_values(self):
        """
        Get the list of portfolio values recorded over time.

        Returns:
        - List[float]: List of portfolio values.
        """
        return self.portfolio_values

    def get_trade_history(self):
        """
        Get the list of all trades made by the portfolio.

        Returns:
        - List[dict]: List of trade details.
        """
        return self.trade_history

    def get_current_holdings(self):
        """
        Get the current asset holdings in the portfolio.

        Returns:
        - dict: A dictionary of symbol -> quantity representing current holdings.
        """
        return self.positions

    def calculate_total_return(self):
        """
        Calculate the total return of the portfolio from the initial capital to the latest portfolio value.

        Returns:
        - float: Total return as a percentage.
        """
        if not self.portfolio_values:
            return 0.0
        latest_value = self.portfolio_values[-1]
        return ((latest_value - self.initial_capital) / self.initial_capital) * 100

    def calculate_portfolio_value(self, current_prices):
        """
        Calculate the total portfolio value based on the current prices of held assets.

        Parameters:
        - current_prices (dict or float): A dictionary of the latest prices for each asset, or a single price
        if only one asset is being traded.
        """
        total_value = self.cash  # Start with available cash

        if isinstance(current_prices, dict):
            # If multiple assets, calculate the value for each symbol
            for symbol, qty in self.positions.items():
                if qty > 0:
                    total_value += qty * current_prices.get(symbol, 0)
        else:
            # If only one asset, calculate the value assuming a single price
            for symbol, qty in self.positions.items():
                if qty > 0:
                    total_value += qty * current_prices  # current_prices is a float here

        self.portfolio_values.append(total_value)


    def calculate_risk_exposure(self):
        """
        Calculate the portfolio's risk exposure by determining the percentage of the portfolio invested in assets
        versus the cash held.

        Returns:
        - float: Risk exposure as a percentage of the portfolio invested in assets.
        """
        if not self.portfolio_values:
            return 0.0
        latest_value = self.portfolio_values[-1]
        invested_value = latest_value - self.cash
        return (invested_value / latest_value) * 100
