# src/my_strategy.py
import pandas as pd
import numpy as np
from src.strategy import Strategy

class MyCustomStrategy(Strategy):
    def generate_signals(self, data):
        signals = pd.Series(index=data.index, dtype=int)
        
        short_window = 40
        long_window = 100
        
        short_mavg = data['Close'].rolling(window=short_window).mean()
        long_mavg = data['Close'].rolling(window=long_window).mean()

        # Golden Cross/Death Cross logic
        signals[(short_mavg > long_mavg)] = 1  # Golden Cross (buy)
        signals[(short_mavg < long_mavg)] = -1  # Death Cross (sell)

        return signals
