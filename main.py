import requests
from bs4 import BeautifulSoup
import pandas as pd
USER_AGENT='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
ACCEPT_LANG='en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7'
header={"User-Agent":USER_AGENT,
        "Accept-Language":ACCEPT_LANG}
url = 'https://www.trulia.com/houses-for-sale-near-me/'
response = requests.get(url, headers=header)
data=response.text
soup = BeautifulSoup(data, "html.parser")
all_link_elements=soup.select("li div div div div div div a")
all_links=[]
for link in all_link_elements:
        href=link["href"]
        if "http" not in href:
                all_links.append(f"https://www.trulia.com/{href}")
        else:
                all_links.append(href)

all_address_elements = soup.select("li div div div div div div a div")
all_addresses = [address.get_text() for address in all_address_elements]

all_price_elements = soup.find_all('div',  {"class":"Text__TextBase-sc-1cait9d-0-div Text__TextContainerBase-sc-1cait9d-1 enhvQK iilDhj"})
all_prices = []
all_prices = [price.get_text() for price in all_price_elements]

dict = {'Address': all_addresses, 'Property Price': all_prices, 'Link': all_links}
df = pd.DataFrame(dict)
print(df)
df.to_csv('Houses in SanFrancisco.csv')
sale_details=pd.read_csv