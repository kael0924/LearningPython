import pandas as pd
import requests

TEST_URL = 'https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes_(seasons_1%E2%80%9320)'

# Need to add this because some sites block the default User-Agent used by urllib and pandas because it identifies the request as automated bot. By providing custom header, you will simulate a request from a standard web browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}

response = requests.get(TEST_URL, headers=headers) #adding the headers when getting the data in the url


tables = pd.read_html(response.text) 
 
print(tables[0])