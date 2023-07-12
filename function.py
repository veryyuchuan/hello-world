
def extract_data(element, dataframe):

    name = element.find('h2').text
    country = element.find('span').text

    year_and_funding = element.find(class_='flex flex-col gap-0')
    website = element.find("a").text
    description = element.find("p").text

    year_and_funding = year_and_funding.text

    # Use regular expressions to extract the founding year
    founding_year_match = re.search(r"Founding Year: (\d+)", year_and_funding)

    if founding_year_match:
        founding_year = founding_year_match.group(1)
        # Build the second part string
        year = founding_year
    else:
        year = ""

    # Use regular expressions to extract the total funding
    total_funding_match = re.search(r"Total Funding: (\$.+)", year_and_funding)

    if total_funding_match:
        total_funding = total_funding_match.group(1)
        # Build the first part string
        funding = total_funding
    else:
        funding = ""

    # Create a dictionary with the new data
    new_data = {
        "Name": [name],
        "Country": [country],
        "Year": [year],
        "Funding": [funding],
        "Website": [website],
        "Description": [description]
    }

    # Create a new dataframe from the new data
    new_dataframe = pd.DataFrame(new_data)

    # Append the new dataframe to the existing dataframe
    data = pd.concat([dataframe, new_dataframe], ignore_index=True)

    return data


def extract_all(url, n)

  response = requests.get(url)
  # create an empty dataframe
  df = pd.DataFrame(columns=['Name', 'Country', 'Year', 'Funding', 'Website', 'Description'])

  # Create a BeautifulSoup object to parse the HTML content
  soup = BeautifulSoup(response.content, "html.parser")

# Find all elements with the specified class
 elements = soup.find(class_="flex flex-col items-start gap-3 rounded-lg border-2 bg-white p-5 dark:bg-slate-900 undefined")

# iterate over 
 for element in elements[:n]:
     df=extract_data(element, df)

# return the data
 return df
