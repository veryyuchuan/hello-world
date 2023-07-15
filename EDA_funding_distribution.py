import pandas as pd
import seaborn as sns

def funding_distribution(data_file, min_funding, max_funding):
    # Load the dataset into a pandas DataFrame
    data = pd.read_csv(data_file)

    # Remove non-numeric characters from funding amounts and convert to float
    data['Funding'] = data['Funding'].str.replace('[^\d.]', '', regex=True).astype(float)

    # Extract the relevant columns for funding analysis
    company_names = data['Name']

    data = data[data['Funding'] != 0]
    data = data[data['Funding'].notna()]

    # Filter data for funding amounts within the specified range
    filtered_data = data[(data['Funding'] >= min_funding) & (data['Funding'] <= max_funding)]

    # Set seaborn style
    sns.set(style="ticks")

    # Set larger figure size and add margin
    plt.figure(figsize=(12, 8))
    plt.subplots_adjust(left=0.1, right=0.9, top=0.7, bottom=0.1)

    # Plot the distribution of funding amounts
    sns.histplot(data=filtered_data, x='Funding', bins=100, kde=True, color='skyblue')
    plt.xlabel('Funding Amount (in Millions of Dollars)')
    plt.ylabel('Number of Companies')
    plt.title(f'Distribution of Funding Amounts ({min_funding}-{max_funding}), in Millions of Dollars')
    plt.xlim(left=min_funding)  # Set the x-axis minimum value
    plt.xticks(ticks=range(int(min_funding), int(max_funding)+1, 100))  # Set custom x-axis ticks

    # Add the total number of companies as a text annotation
    total_companies = len(filtered_data)
    plt.text(0.95, 0.95, f'Total Companies: {total_companies}', ha='right', va='top', transform=plt.gca().transAxes)

    plt.show()

