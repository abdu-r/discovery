import pandas as pd
import encrypt

# Decrypt data file
encryted_file_name = 'data/enc_best.csv'
decryppted_file_name = 'data/best_dec.csv'
key_file_name = 'data/enc.key'
key = encrypt.get_key(key_file_name)
encrypt.decrypt_file(key, encryted_file_name, decryppted_file_name)

# Load data
df = pd.read_csv('data/best_dec.csv')
# check data types
# print(df.dtypes)
# print('------------------------------ Loaded Data ---------------------------------------------------------------')
# print(df.head(5))
# print('----------------------------------------------------------------------------------------------------------')

# print('---------------------------------- Get Statistics ------------------------------------------------------------------')
# print(df.describe())
# print('-----------------------------------------------------------------------------------------------------------------')

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

# Write compress file
df.to_csv('data/result.csv.zip', index=False, compression='zip')

# Encrypt compressed file
# encrypted_output_file = 'data/enc_best_out.csv'
# encrypt.encrypt_file(key, 'data/result.csv.zip', encrypted_output_file)

# encrypt.decrypt_file(key, encrypted_output_file, 'data/final.csv.zip')


