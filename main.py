import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

url = "https://mad.firstmark.com/card"
n = 10



extract_all(url, n)

