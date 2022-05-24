import pandas as pd
import numpy as np

# Load data
df = pd.read_csv('data/best_seller.csv')
# check data types
# print(df.dtypes)
# print('------------------------------ Loaded Data ---------------------------------------------------------------')
# print(df)
# print('----------------------------------------------------------------------------------------------------------')

print('---------------------------------- Get Statistics ------------------------------------------------------------------')
print(df.describe())
print('-----------------------------------------------------------------------------------------------------------------')

# Remove unwanted coulumns
df.drop(['Name', 'Genre'], axis=1, inplace=True)
# print('------------------------------ Data Types after Removing Name and Genre columns -----------------------------')
# print(df.dtypes)
# print('-------------------------------------------------------------------------------------------------------------')

# Remove unwanted rows
print(df.shape[0])
df.drop(df[df['Price'] >= 10].index, inplace = True)
# print('------------------------------ Data After Removing Price Less Than 10 -----------------------------------------')
# print(df.shape[0])
# print('----------------------------------------------------------------------------------------------------------------')

# Show the columns that have nulls
null_cols = [i for i in df.columns if df[i].isnull().any()]
# print('------------------------------ Show Columns That Contain NULL --------------------------------------------------')
# print(null_cols)
# print('----------------------------------------------------------------------------------------------------------------')

# Replacing null
df['Reviews'] =  df['Reviews'].fillna(0) # Replace null in one column
avg_price = int(df['Price'].mean())
df =  df.fillna(value={'User Rating':0,'Price':avg_price}) # Replace null in multiple column
# print('--------------------------- Average price --------------------------------------------------------------------------')
# print(avg_price)
# print(df[df['Price'] == 6])

col_with_null = [i for i in df.columns if df[i].isnull().any()]
# print('------------------------------ Check That There No Columns With Null Values  -------------------------------------------')
# print(col_with_null)
# print('------------------------------------------------------------------------------------------------------------------------')

# data conversation example
df['Year'] = pd.to_datetime(df['Year'], format='%Y') # convert int to year
df['Reviews'] = df['Reviews'].astype(int) # convert float to int
# print('------------------------------ Check Data Types After Conversion -------------------------------------------------------')
# print(df.dtypes)
# print('------------------------------------------------------------------------------------------------------------------------')





