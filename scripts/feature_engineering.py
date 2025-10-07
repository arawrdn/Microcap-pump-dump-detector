import pandas as pd

df = pd.read_csv('../data/microcap_tokens.csv', parse_dates=['timestamp'])

# Example features
df['price_change'] = df['price'].pct_change()
df['volume_change'] = df['volume'].pct_change()
df['price_ma7'] = df['price'].rolling(7).mean()
df['volume_ma7'] = df['volume'].rolling(7).mean()

df.dropna(inplace=True)
df.to_csv('../data/features.csv', index=False)
print("Features saved to data/features.csv")
