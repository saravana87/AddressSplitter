import pandas as pd
from postal.parser import parse_address

# Read CSV file into a DataFrame
df = pd.read_csv('Addresses.csv', encoding='Windows-1252')
# Function to parse addresses
def parse_address_components(address):
    parsed = parse_address(address)
    components = {
        "house_number": None,
        "road": None,
        "city": None,
        "state": None,
        "postcode": None
    }
    
    # Store parsed components in a dictionary
    for component, label in parsed:
        if label == 'house_number':
            components['house_number'] = component
        elif label == 'road':
            components['road'] = component
        elif label == 'city':
            components['city'] = component
        elif label == 'state':
            components['state'] = component
        elif label == 'postcode':
            components['postcode'] = component
    
    return components
df['Address'] = df['Address'].astype(str).fillna('')

# Apply the function to the 'address' column
df[['house_number', 'road', 'city', 'state', 'postcode']] = df['Address'].apply(
    lambda address: pd.Series(parse_address_components(address))
)

# Output the result
print(df)

# Optionally, save to a new CSV
df.to_csv('parsed_addresses.csv', index=False)
