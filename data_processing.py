import csv
import os

input_folder = 'data'
output_file = 'data_sales_data_pink_morsel.csv'

combined_data = []

for filename in os.listdir(input_folder):
    if filename.endswith('.csv'):
        file_path = os.path.join(input_folder, filename)

        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row['product'] == 'pink morsel':
                    row['price'] = float(row['price'][1:])
                    row['sales'] = row['price'] * int(row['quantity'])

                    combined_data.append(row)

combined_data.sort(key=lambda x: x['date'])

output_data = [
    {'sales': row['sales'], 'date': row['date'], 'region': row['region']}
    for row in combined_data
]

with open(output_file, 'w', newline='') as file:
    fieldnames = ['sales', 'date', 'region']
    writer = csv.DictWriter(file, fieldnames=fieldnames);
    writer.writeheader()
    writer.writerows(output_data)
