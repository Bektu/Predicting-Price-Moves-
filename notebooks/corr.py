import pandas as pd
import talib
import numpy as np

def add_more_indicators(df):
    close = df['close'].values
    # Relative Strength Index
    df['rsi_14'] = talib.RSI(close, timeperiod=14)
    # MACD
    macd, macd_signal, macd_hist = talib.MACD(close, fastperiod=12, slowperiod=26, signalperiod=9)
    df['macd'] = macd
    df['macd_signal'] = macd_signal
    df['macd_hist'] = macd_hist

    return df
