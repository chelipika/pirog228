from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from logins import loggins
if input("Do you wanna run? ") == "y":
    driver = webdriver.Chrome()
    driver.get("https://login.emaktab.uz")
    for acc in loggins:
        elem = driver.find_element(By.NAME, "login")
        elem.clear()
        elem.send_keys(acc['login'])
        elem.send_keys(Keys.RETURN)
        elem2 = driver.find_element(By.NAME, "password")
        elem2.clear()
        elem2.send_keys(acc['password'])
        elem2.send_keys(Keys.RETURN)
        elem3 = driver.find_element(By.NAME, "logout")
        elem3.click()
        
    
    driver.close()

else:
    print("Weel done fren")

# print(loggins[0]['login'])
