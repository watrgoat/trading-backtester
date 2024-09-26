from abc import ABC, abstractmethod

class Strategy(ABC):
    def __init__(self, params=None):
        """
        Initialize the strategy with optional parameters.
        
        Parameters:
        - params (dict): A dictionary of parameters, like window sizes, thresholds, etc.
        """
        self.params = params if params is not None else {}

    @abstractmethod
    def generate_signals(self, data):
        """
        Generate buy/sell signals from the data.
        
        This method must be implemented by user-defined strategies.
        """
        pass

