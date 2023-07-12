import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

url = "https://mad.firstmark.com/card"
n = 10

#create a csv file
data = extract_all(url, n)
data.to_csv('data.csv')
