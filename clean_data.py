import pandas as pd

# Load the raw CSV file with all columns as strings
df = pd.read_csv('Assignment-5/ebay_tech_deals.csv', dtype=str)

# Clean the price column by removing "US $" and commas, and trim extra whitespace
df['price'] = df['price'].str.replace('US $', '', regex=False).str.replace(',', '').str.strip()

# If original_price column does not exist, create it and populate it with the same values as price
if 'original_price' not in df.columns:
    df['original_price'] = df['price']

# Clean the original_price column by removing "US $" and commas, and trim extra whitespace
df['original_price'] = df['original_price'].str.replace('US $', '', regex=False).str.replace(',', '').str.strip()

# If original_price is missing (i.e., marked as "N/A" or empty), replace it with the corresponding price
df['original_price'] = df['original_price'].replace({'N/A': None, '': None})
df['original_price'] = df['original_price'].fillna(df['price'])

# Clean the shipping column by replacing "N/A", empty strings, or strings containing only whitespace with the default message
if 'shipping' in df.columns:
    df['shipping'] = df['shipping'].replace({'N/A': 'Shipping info unavailable', '': 'Shipping info unavailable'})
    df['shipping'] = df['shipping'].fillna('Shipping info unavailable')
else:
    df['shipping'] = 'Shipping info unavailable'

# Convert the price and original_price columns to numeric (float) values
df['price'] = pd.to_numeric(df['price'], errors='coerce')
df['original_price'] = pd.to_numeric(df['original_price'], errors='coerce')

# Create a new column discount_percentage computed as:
# discount_percentage = (1 - (price / original_price)) * 100
df['discount_percentage'] = ((1 - (df['price'] / df['original_price'])) * 100).round(2)

# Handle missing values in discount_percentage (e.g., when original_price is 0 or NaN)
df['discount_percentage'] = df['discount_percentage'].fillna(0)

# Save the cleaned data as cleaned_ebay_deals.csv
df.to_csv('Assignment-5/cleaned_ebay_deals.csv', index=False)

print("Data cleaning and processing completed. Cleaned data saved as 'cleaned_ebay_deals.csv'.")