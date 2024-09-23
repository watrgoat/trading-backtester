# src/portfolio.py
class Portfolio:
    def __init__(self, initial_capital):
        self.initial_capital = initial_capital
        self.cash = initial_capital
        self.positions = {}
        self.portfolio_values = []
    
    def update_holdings(self, trade):
        symbol = trade['symbol']
        qty = trade['quantity']
        price = trade['price']
        if trade['type'] == 'buy':
            self.cash -= qty * price
            self.positions[symbol] = self.positions.get(symbol, 0) + qty
        elif trade['type'] == 'sell':
            self.cash += qty * price
            self.positions[symbol] = self.positions.get(symbol, 0) - qty
        self.calculate_portfolio_value(price)
    
    def calculate_portfolio_value(self, current_price):
        total = self.cash
        for symbol, qty in self.positions.items():
            total += qty * current_price
        self.portfolio_values.append(total)
    
    def get_portfolio_values(self):
        return self.portfolio_values