import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import functions

url = "https://mad.firstmark.com/card"

#create a csv file
data = functions.extract_all(url)
data.to_csv('data.csv')
