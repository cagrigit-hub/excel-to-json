import pandas as pd

# Replace 'your_excel_file.xlsx' with the path to your actual Excel file
excel_file = 'new_winner_List.xlsx'

# Read the Excel file into a Pandas DataFrame
df = pd.read_excel(excel_file)

# Extract the 'address' column and convert the addresses to lowercase and wrap them in double quotes
addresses = df['address'].str.lower().apply(lambda x: '"' + x + '"').tolist()

# Concatenate the addresses into a single string with commas
addresses_string = ','.join(addresses)

# Replace 'output_file.txt' with the path and name of the text file where you want to save the addresses
output_file = 'output_file.json'

# Save the addresses to a text file
with open(output_file, 'w') as file:
    file.write("[" + addresses_string + "]")

print("Addresses have been saved to the text file.")
