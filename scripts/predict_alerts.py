import pandas as pd
import pickle

df = pd.read_csv('../data/features.csv')
model = pickle.load(open('../data/model.pkl', 'rb'))

X = df[['price_change', 'volume_change', 'price_ma7', 'volume_ma7']]
df['prediction'] = model.predict(X)

alerts = df[df['prediction'] == 1]
print("Detected pump alerts:")
print(alerts[['timestamp', 'price', 'volume']])
