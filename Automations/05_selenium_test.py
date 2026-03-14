from selenium import webdriver
from selenium.webdriver.chrome.service import Service


website_url = "https://www.thesun.co.uk/sport/football/"


driver = webdriver.Chrome()

driver.get(website_url)
