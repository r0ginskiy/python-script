import requests
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://www.europages.co.uk/companies/manufacturers.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


elements = soup.find_all('p') 


data = [element.text.strip() for element in elements if element.text.strip()]


df = pd.DataFrame(data, columns=['Data'])
df.to_excel('data.xlsx', index=False)

print("Данные успешно сохранены в data.xlsx")
