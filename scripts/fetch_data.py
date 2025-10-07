```python
import requests
import pandas as pd

token_id = "shiba-inu"
url = f"https://api.coingecko.com/api/v3/coins/{token_id}/market_chart?vs_currency=usd&days=90&interval=daily"

response = requests.get(url)
data = response.json()

prices = pd.DataFrame(data['prices'], columns=['timestamp', 'price'])
volumes = pd.DataFrame(data['total_volumes'], columns=['timestamp', 'volume'])

df = prices.merge(volumes, on='timestamp')
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
df.to_csv('../data/microcap_tokens.csv', index=False)

print("Fetched data saved to data/microcap_tokens.csv")
