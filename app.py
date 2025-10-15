import pandas as pd


df = pd.read_csv('text.csv')


print(df.isnull().sum())

# print(df.head(10))

print(df["Coffee Consumption"].value_counts(dropna=False))


print(df['Sleep Hours'].skew())

print(df.info())

df['Coffee Consumption'].fillna(df['Coffee Consumption'].mode()[0], inplace=True)


print(df.isnull().sum())


# print(df.head(50))

df = pd.get_dummies(df, columns=['Coffee Consumption'], drop_first=False)


print(df.head(10))