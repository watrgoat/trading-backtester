# src/execution_handler.py

class ExecutionHandler:
    def __init__(self, transaction_cost=0.001):
        self.transaction_cost = transaction_cost

    def execute_order(self, order):
        # Simulate slippage by adjusting price slightly
        slippage_factor = 0.0005  # 0.05%
        if order['type'] == 'buy':
            executed_price = order['price'] * (1 + slippage_factor)
        elif order['type'] == 'sell':
            executed_price = order['price'] * (1 - slippage_factor)
        else:
            raise ValueError("Order type must be 'buy' or 'sell'")

        cost = order['quantity'] * executed_price * self.transaction_cost
        
        # Create trade dictionary, including the 'date' key
        trade = {
            'symbol': order['symbol'],
            'type': order['type'],
            'quantity': order['quantity'],
            'price': executed_price,
            'cost': cost,
            'date': order['date']  # Include the date in the trade dictionary
        }
        return trade
