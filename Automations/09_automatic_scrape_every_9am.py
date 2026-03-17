import sys
import os
import pandas as pd
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from datetime import datetime




web_url = "https://www.lamudi.com.ph/buy/metro-manila/house/"



options = Options()
options.headless=True
driver = webdriver.Chrome(options=options)


application_path = os.path.dirname(sys.executable)
now = datetime.now()
month_day_year = now.strftime("%m%d%Y")

driver.get(web_url) # open web url
time.sleep(5)

containers = driver.find_elements(by="xpath", value="//*[starts-with(@class, 'snippet js-snippet normal')]")

property_names = []
property_locations = []
property_descriptions = []
property_prices = []
property_links = []


for container in containers:
  property_name = container.find_element(by="xpath", value=".//div/a/div/span").text
  property_location = container.find_element(by="xpath", value=".//*[starts-with(@class, 'snippet__content__location')]/span").text
  property_description = container.find_element(by="xpath", value=".//*[starts-with(@class, 'snippet__content__description')]").text
  property_price = container.find_element(by="xpath", value=".//*[starts-with(@class, 'snippet__content__price')]").text
  property_link = container.find_element(by="xpath", value="./div/a").get_attribute("href")

  # append
  property_names.append(property_name)
  property_locations.append(property_location)
  property_descriptions.append(property_description)
  property_prices.append(property_price)
  property_links.append(property_link)


excel_layout = {
  'Property Name': property_names,
  'Property Description': property_descriptions,
  'Property Locations': property_locations,
  'Property Price': property_prices,
  'Property Links': property_links
}

data_frame = pd.DataFrame(excel_layout)

file_name = f"lamudi-{month_day_year}.csv"
final_path = os.path.join(application_path, file_name) # join application  path and filename avoid the /

data_frame.to_csv(final_path)


driver.quit()
