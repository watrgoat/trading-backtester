# examples/my_strategy.py

import pandas as pd
from src.strategy import Strategy

class MyCustomStrategy(Strategy):
    def generate_signals(self, data):
        signals = pd.Series(index=data.index, dtype=int)
        short_window = 40
        long_window = 100
        
        short_mavg = data['Close'].rolling(window=short_window).mean()
        long_mavg = data['Close'].rolling(window=long_window).mean()
        
        signals[data['Close'] > short_mavg] = 1
        signals[data['Close'] < long_mavg] = -1
        
        return signals

class MovingAverageStrategy(Strategy):
    def generate_signals(self, data):
        short_window = self.params.get('short_window', 40)
        long_window = self.params.get('long_window', 100)
        
        short_mavg = data['Close'].rolling(window=short_window).mean()
        long_mavg = data['Close'].rolling(window=long_window).mean()
        
        signals = pd.Series(index=data.index, dtype=int)
        signals[data['Close'] > short_mavg] = 1
        signals[data['Close'] < long_mavg] = -1
        
        return signals
