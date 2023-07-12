import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import functions

url = "https://mad.firstmark.com/card"
n = 10

#create a csv file
data = functions.extract_all(url, n)
data.to_csv('data.csv')
