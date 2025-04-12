import requests  
from bs4 import BeautifulSoup  
import pandas as pd  

# 1. Scrape IMDb Top 10  
url = "https://www.imdb.com/chart/top/"  
headers = {'User-Agent': 'Mozilla/5.0'}  
response = requests.get(url, headers=headers)  
soup = BeautifulSoup(response.text, 'html.parser')  

# 2. Extract data  
movies = []  
for row in soup.select('.ipc-metadata-list li'):  # Top 10 only  
    title = row.find('h3', class_='ipc-title__text').text
    movies.append({'title': title})  

# 3. Save as CSV  
imdb_df = pd.DataFrame(movies)  
imdb_df.to_csv("imdb_top10.csv", index=False)  
print("Saved IMDb data!")  