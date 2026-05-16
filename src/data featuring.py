import pandas as pd

apple = pd.read_csv('AAPL_cleaned.csv')

# RETURNS
apple['Return'] = apple['Close'].pct_change()

# MOVING AVERAGES
apple['MA_7'] = apple['Close'].rolling(7).mean()
apple['MA_21'] = apple['Close'].rolling(21).mean()
apple['MA_50'] = apple['Close'].rolling(50).mean()

# VOLATILITY
apple['Volatility_7'] = apple['Return'].rolling(7).std()
apple['Volatility_21'] = apple['Return'].rolling(21).std()
apple['Volatility_50'] = apple['Return'].rolling(50).std()

# ---------------- RSI ----------------

delta = apple['Close'].diff()

gain = delta.where(delta > 0, 0)
loss = -delta.where(delta < 0, 0)

avg_gain = gain.rolling(14).mean()
avg_loss = loss.rolling(14).mean()

rs = avg_gain / avg_loss

apple['RSI'] = 100 - (100 / (1 + rs))

# ---------------- MACD ----------------

ema_12 = apple['Close'].ewm(span=12, adjust=False).mean()
ema_26 = apple['Close'].ewm(span=26, adjust=False).mean()

apple['MACD'] = ema_12 - ema_26

# ---------------- TARGET VARIABLE ----------------

apple['Target'] = (
    apple['Close'].shift(-1) > apple['Close']
).astype(int)

# REMOVE NaN ROWS
apple.dropna(inplace=True)

# SAVE UPDATED DATASET
apple.to_csv('AAPL_cleaned.csv', index=False)

print(apple.tail())
