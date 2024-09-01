from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def webtest():
    driver = webdriver.Chrome(service=Service())
    driver.implicitly_wait(10)

    driver.get('http://localhost:5000/users/get_user_data/1')
    elements = driver.find_element(By.ID, value='user')

    if (elements):
        print(elements.text.split(' ')[1])

