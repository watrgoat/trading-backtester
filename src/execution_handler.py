
class ExecutionHandler:
    def __init__(self, transaction_cost=0.001, slippage_factor=0.0005):
        """
        Initializes the execution handler responsible for executing buy and sell orders.
        
        Parameters:
        - transaction_cost (float): The cost of executing each trade, as a percentage of the trade value.
        - slippage_factor (float): The slippage applied to the order, as a percentage. This represents the 
                                   difference between the expected and actual execution price.
        """
        self.transaction_cost = transaction_cost
        self.slippage_factor = slippage_factor

    def execute_order(self, order):
        """
        Executes a buy or sell order with slippage and transaction costs applied.
        
        Parameters:
        - order (dict): A dictionary containing order details, e.g.:
            {
                'symbol': 'AAPL',
                'type': 'buy' or 'sell',
                'quantity': 10,
                'price': 150.0,
                'date': '2023-01-01'
            }
        
        Returns:
        - trade (dict): A dictionary representing the executed trade, including final price and cost.
        """
        # Apply slippage based on the type of order
        if order['type'] == 'buy':
            executed_price = order['price'] * (1 + self.slippage_factor)  # Slippage increases buy price
        elif order['type'] == 'sell':
            executed_price = order['price'] * (1 - self.slippage_factor)  # Slippage decreases sell price
        else:
            raise ValueError("Order type must be 'buy' or 'sell'")  # Error handling for invalid order types

        # Calculate the cost of the trade (quantity * price * transaction cost)
        trade_cost = order['quantity'] * executed_price * self.transaction_cost
        
        # Construct the trade dictionary, capturing the essential details
        trade = {
            'symbol': order['symbol'],
            'type': order['type'],
            'quantity': order['quantity'],
            'price': executed_price,  # Final price after slippage
            'cost': trade_cost,  # Total transaction cost
            'date': order['date']  # Trade date passed from the order
        }
        
        return trade

