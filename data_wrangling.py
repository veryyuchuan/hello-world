import pandas as pd


# checking duplicate records
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
