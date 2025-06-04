import pandas as pd
import talib
import numpy as np

def add_technical_indicators(df):
    # If MultiIndex, flatten
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(1)

    df = df.sort_values('date').copy()

    # Ensure numeric types
    df['close'] = pd.to_numeric(df['close'], errors='coerce')
    df['high'] = pd.to_numeric(df['high'], errors='coerce')
    df['low'] = pd.to_numeric(df['low'], errors='coerce')

    # Ensure no bad shapes
    close = df['close'].values.astype(float)
    high = df['high'].values.astype(float)
    low = df['low'].values.astype(float)

    df['daily_return'] = df['close'].pct_change()
    df['sma_10'] = talib.SMA(close, timeperiod=10)
    df['ema_10'] = talib.EMA(close, timeperiod=10)
    df['atr'] = talib.ATR(high, low, close, timeperiod=14)
    df['boll_upper'], df['boll_middle'], df['boll_lower'] = talib.BBANDS(close)

    return df
def describe_price_statistics(df):
    cols = ['close', 'daily_return', 'sma_10', 'ema_10', 'atr']
    existing = [c for c in cols if c in df.columns]
    return df[existing].describe()
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
