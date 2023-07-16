import pandas as pd


# check duplicate records
def check_duplicates(data_file):
    # Load the dataset into a pandas DataFrame
    data = pd.read_csv(data_file)

    # Check for duplicate records
    duplicate_records = data[data.duplicated()]

    # Print the duplicate records
    if not duplicate_records.empty:
        print("Duplicate records:")
        print(duplicate_records)
    else:
        print("No duplicate records found.")

# remove duplicate records
def remove_duplicates(data_file):
    # Load the dataset into a pandas DataFrame
    data = pd.read_csv(data_file)

    # Remove duplicate records
    data = data.drop_duplicates()

    # Save the cleaned data to a new file
    cleaned_file = 'cleaned_' + data_file
    data.to_csv(cleaned_file, index=False)

    print("Duplicate records removed. Cleaned data saved to", cleaned_file)
