# src/execution_handler.py
class ExecutionHandler:
    def __init__(self, transaction_cost=0.001):
        self.transaction_cost = transaction_cost
    
    def execute_order(self, order):
        # Simulate slippage by adjusting price slightly
        slippage = order['price'] * 0.0005
        executed_price = order['price'] + slippage if order['type'] == 'buy' else order['price'] - slippage
        cost = order['quantity'] * executed_price * self.transaction_cost
        trade = {
            'symbol': order['symbol'],
            'type': order['type'],
            'quantity': order['quantity'],
            'price': executed_price,
            'cost': cost
        }
        return trade