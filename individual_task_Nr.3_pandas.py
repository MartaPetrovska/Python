import pandas as pd
prices = pd.read_csv('/content/prices.txt', header = None, delimiter = ' ')
prices.columns = ['Price']
prices['Price'] = pd.to_numeric(prices['Price'], errors='coerce')
prices.dropna(subset=['Price'], inplace=True)
prices.reset_index(drop=True, inplace=True)
print(prices)
print(f"Total value: {prices['Price'].sum()}")
print(f"Items purchased: {prices['Price'].count()}")
