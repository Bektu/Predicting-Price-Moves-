import talib

def calculate_moving_average(df, period=10):
    df[f'MA_{period}'] = talib.SMA(df['Close'], timeperiod=period)
    return df

def calculate_rsi(df, period=14):
    df['RSI'] = talib.RSI(df['Close'], timeperiod=period)
    return df

def calculate_macd(df):
    macd, macdsignal, macdhist = talib.MACD(df['Close'])
    df['MACD'] = macd
    df['MACD_signal'] = macdsignal
    return df