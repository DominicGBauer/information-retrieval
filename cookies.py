import pickle
import pprint

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

def save_cookies(driver, location):
    pickle.dump(driver.get_cookies(), open(location, "wb"))


def load_cookies(driver, location, url=None):
    cookies = pickle.load(open(location, "rb"))
    driver.delete_all_cookies()
   
    driver.get("https://vula.uct.ac.za" if url is None else url)
    for cookie in cookies:
        if isinstance(cookie.get('expiry'), float):
            cookie['expiry'] = int(cookie['expiry'])
        driver.add_cookie(cookie)


def delete_cookies(driver, domains=None):
    if domains is not None:
        cookies = driver.get_cookies()
        original_len = len(cookies)
        for cookie in cookies:
            if str(cookie["domain"]) in domains:
                cookies.remove(cookie)
        if len(cookies) < original_len:  
         
            driver.delete_all_cookies()
            for cookie in cookies:
                driver.add_cookie(cookie)
    else:
        driver.delete_all_cookies()


cookies_location = "C:\Users\User\Desktop\MPhil\chrome\chromedriver\cookies.txt"


username= "" # provide uct email studentNo@myuct.ac.za
password="" #uct vula password


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www-jstor-org.ezproxy.uct.ac.za')

 
driver.find_element_by_xpath(".//input[@id='userNameInput']").send_keys(username)
driver.find_element_by_xpath(".//input[@id='passwordInput']").send_keys(password)
driver.find_element_by_xpath(".//span[@id='submitButton']").click()
sleep(3)

