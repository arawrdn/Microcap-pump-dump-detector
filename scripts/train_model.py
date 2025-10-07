import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
import pickle

df = pd.read_csv('../data/features.csv')

# Example: label pump/dump manually for demo (1=pump, 0=normal)
df['label'] = (df['price_change'] > 0.1).astype(int)

X = df[['price_change', 'volume_change', 'price_ma7', 'volume_ma7']]
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

model = XGBClassifier()
model.fit(X_train, y_train)

pickle.dump(model, open('../data/model.pkl', 'wb'))
print("Model trained and saved to data/model.pkl")
