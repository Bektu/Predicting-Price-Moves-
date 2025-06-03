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