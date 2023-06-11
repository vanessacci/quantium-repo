import pandas as pd

file1 = pd.read_csv('data/daily_sales_data_0.csv')
file2 = pd.read_csv('data/daily_sales_data_1.csv')
file3 = pd.read_csv('data/daily_sales_data_2.csv')

files = [file1, file2, file3]

for file in files:
    file = file[file['product'] == 'pink morsel']

for file in files:
    file['sales'] = file['price'] * file['quantity']

for file in files:
    file = file['sales', 'data', 'region']

output_data = pd.concat(files)
output_data.to_csv('daily_sales_data_pink_morsels', index=False)
