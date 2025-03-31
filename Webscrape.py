from bs4 import BeautifulSoup
import requests
import pandas as pd

geolocator = Nominatim(user_agent='car_sales_geocoder')
r = requests.get('https://en.wikipedia.org/wiki/List_of_best-selling_automobiles')
soup = BeautifulSoup(r.text, 'html.parser')
tables = soup.find_all('table', class_='wikitable')
table = tables[1]
if tables:
    table = tables[1]
    rows = table.find_all('tr')

data = []
for row in rows:
    cols = row.find_all('td')

    if len(cols) > 3:
        country = cols[0].get_text(strip=True)
        automobile = cols[1].get_text(strip=True)
        years_sold = cols[2].get_text(strip=True)
        notes = cols[3].get_text(strip=True)

        # Print the extracted information
        data.append([country, automobile, years_sold, notes])
df = pd.DataFrame(data, columns=['Country', 'Automobile', 'Years_Sold', 'Notes'])
