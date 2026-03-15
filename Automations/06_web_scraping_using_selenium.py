from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd

website_url = "https://www.thesun.co.uk/sport/football/"
fullnovel_url = "https://novelfull.net/"


driver = webdriver.Chrome()
driver.get(fullnovel_url)
time.sleep(5)


containers = driver.find_elements(by="xpath", value="//*[starts-with(@class, 'item top-')]") # find elements vs find element

titles = []
links = []

for container in containers:
    title = container.find_element(by="xpath", value="./a/div/h3").text
    link = container.find_element(by="xpath", value="./a").get_attribute("href")


    titles.append(title)
    links.append(link)

fullnovel_dict = {'Title': titles, 'Link': links}

df_headlines = pd.DataFrame(fullnovel_dict)
df_headlines.to_csv('06_headline.csv')


driver.quit()