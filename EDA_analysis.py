import pandas as pd
import seaborn as sns


# funding distribution
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


# Geographic analysis: number of companies grouped by country
def geographic_analysis(data_file):
    # Load the dataset into a pandas DataFrame
    data = pd.read_csv(data_file)
    data.loc[data['Country'] == 'Total Funding: $0.7M', 'Country'] = 'China'

    # Group the data by country and count the number of companies per country
    companies_per_country = data['Country'].value_counts().reset_index()
    companies_per_country.columns = ['Country', 'Count']

    # Sort the data by count in descending order
    companies_per_country = companies_per_country.sort_values('Count', ascending=False)

    # Plot the histogram
    plt.figure(figsize=(12, 6))
    bars = plt.bar(companies_per_country['Country'], companies_per_country['Count'], color='skyblue')
    plt.xlabel('Country')
    plt.ylabel('Number of Companies')
    plt.title('Number of Companies by Country')
    plt.xticks(rotation=45, ha='right')

    # Add numeric labels to each bar
    for bar in bars:
        height = bar.get_height()
        plt.annotate(f'{height}', xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(0, 3), textcoords='offset points', ha='center', va='bottom')

    plt.show()
