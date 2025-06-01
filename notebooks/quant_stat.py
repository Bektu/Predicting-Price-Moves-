# quant_stats.py
pip instal talib
import pandas as pd
import talib

def add_technical_indicators(df):
    df = df.sort_values('date')  # Make sure it's sorted

    # Calculate returns
    df['daily_return'] = df['close'].pct_change()

    # Moving Averages
    df['sma_10'] = talib.SMA(df['close'], timeperiod=10)
    df['ema_10'] = talib.EMA(df['close'], timeperiod=10)

    # Volatility Indicators
    df['atr'] = talib.ATR(df['high'], df['low'], df['close'], timeperiod=14)
    df['boll_upper'], df['boll_middle'], df['boll_lower'] = talib.BBANDS(df['close'])

    return df

def describe_price_statistics(df):
    summary = df[['close', 'daily_return', 'sma_10', 'ema_10', 'atr']].describe()
    return summary
