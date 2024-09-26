import logging

class Logger:
    def __init__(self, log_file='backtest.log'):
        """
        Initialize the logger to write to a specified log file.
        
        - log_file (str): The file where log messages are written. Default is 'backtest.log'.
        
        We use filemode='w' to wipe the log file each time a new run starts.
        """
        logging.basicConfig(filename=log_file, level=logging.INFO, filemode='w',  # Wipe file on each run
                            format='%(message)s')  # Only log the message, not system date

    def log_trade(self, trade):
        """
        Log a trade to the log file.
        
        This method logs only the trade date and message, without including the current system time.
        
        Parameters:
        - trade (dict): A dictionary containing trade information (symbol, type, quantity, price, and date).
        """
        # Format the trade message to only include the trade's date and details
        message = f"{trade['date']} - {trade['type'].upper()} {trade['quantity']} {trade['symbol']} at {trade['price']:.2f}"
        logging.info(message)

    def log_error(self, message):
        """
        Log an error message.
        
        Parameters:
        - message (str): The error message to be logged.
        """
        logging.error(message)

    def log_event(self, message):
        """
        Log a general event.
        
        Parameters:
        - message (str): The event message to be logged.
        """
        logging.info(message)

    def log_warning(self, message):
        """
        Log a warning message.
        
        Parameters:
        - message (str): The warning message to be logged.
        """
        logging.warning(message)
