import pandas as pd

apple = pd.read_csv("AAPL_stock_data.csv")
apple = apple.iloc[2:]
apple.columns = ['Date', 'Close', 'High', 'Low', 'Open', 'Volume']

apple['Date'] = pd.to_datetime(apple['Date'])
numeric_cols = ['Close', 'High', 'Low', 'Open', 'Volume']
for col in numeric_cols:
    apple[col] = pd.to_numeric(apple[col], errors='coerce')

apple.dropna(inplace=True)
apple.drop_duplicates(inplace=True)
apple.sort_values('Date', inplace=True)
apple.reset_index(drop=True, inplace=True)

apple.to_csv("AAPL_cleaned.csv", index=False)
