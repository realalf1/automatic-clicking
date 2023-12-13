from selenium import webdriver
from selenium.webdriver.common.by import By

def clickclick(url, location, element_class, limit=1):
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(url)

    button = driver.find_element(element_class, location)

    counter = 0
    while counter < limit:
        button.click()
        counter = counter + 1

clickclick("url","class", By.ID, 10)
