import pandas as pd

train_df = pd.read_csv('train.csv')
print(train_df["Survived"])
train_df['Sex'] = train_df['Sex'].map({'female': 1, 'male': 0}).astype(int)
print(train_df["Sex"])
print("correltaion value is :",train_df['Survived'].corr(train_df['Sex']))
