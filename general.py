#pip install undetected-chromedriver

#pip install setuptools

#https://googlechromelabs.github.io/chrome-for-testing/#stable

import requests
import time
import selenium
import os
import csv
import undetected_chromedriver as uc 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pandas as pd

uc.Chrome.__del__ = lambda self: None #фикс ошибка с закрытием(первый промт в клоде)

class Parcer():

    def __init__(self, link, klas):
        self.link = link
        self.klas = klas
        chrome_156_path = r"D:\chrome-win64\chrome.exe"
        
        # if not os.path.exists(chrome_156_path): #если не существует, то выведем ошибку
        #     raise FileNotFoundError(f"Не удалось найти Chrome по пути: {chrome_156_path}. Проверьте имя папки.")

        self.options = uc.ChromeOptions()

        self.driver = uc.Chrome(options=self.options, browser_executable_path=chrome_156_path)
        self.driver.get(self.link)

        time.sleep(10)



    def accept_cookie(self):
        click_elem = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "cookies__btn")))
        click_elem.click()
        time.sleep(1)

    def scroll(self, times=17):
        for _ in range(times):
            self.driver.execute_script("window.scrollBy(0, 1000);") #на 2к пикселей вниз и так 9 шагов
            time.sleep(1)



    def getlinks(self):

        time.sleep(2)
        elements_first_page = self.driver.find_elements(By.CLASS_NAME, self.klas)
        links_list = []
        text_list = []
        dictik = {}
        time.sleep(9)

        for element in elements_first_page:
            url = element.get_attribute('href')
            text = element.get_attribute('aria-label')
            links_list.append(url)
            name = text.lower()
            if 'superlight 2' in name:
                text_list.append(text)

        print(links_list)
        print(text_list)
        print(len(links_list))
        print(len(text_list))

        for href in links_list:
            self.driver.get(href)
            characteristik = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "btnDetail--OZvtD")))
            characteristik.click()
            time.sleep(1)
            thes = self.driver.find_elements(By.TAG_NAME, 'th')
            tdes = self.driver.find_elements(By.TAG_NAME, 'td')

            for th , td in zip(thes,tdes):
                key = th.text
                value = td.text

                dictik[key] = value

            file_ext = os.path.isfile("var.csv")
            with open("var.csv", mode="a", encoding="utf-8", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=dictik.keys())

                if not file_ext:
                    writer.writeheader()

                writer.writerow(dictik)


            




    def close(self): #фикс ошибка с закрытием(первый промт в клоде)
        if self.driver:
            try:
                self.driver.quit()
            except OSError:
                pass
            finally:
                self.driver = None    

    # def agent(self):
    #     options = Options()
    #     options.add_argument("--user-agent=Godzilla/5.0 (Windows NT 666.0; Win864; x864) AppleWebKit/537.36 (KHTML, like Gecko) Shrone/120.0.0.0 Safari/537.36")

    #     driver = webdriver.Chrome(options=options)
    #     driver.get('https://whatmyuseragent.com/')
    #     time.sleep(10)
    #     driver.quit()


    # def get_proxy() -> str:

    #     arr = {}
    #     #Сюда нужно поместить ссылку на сайт с проксями
    #     r = requests.get("https://advanced.name/freeproxy/6adc585c6b0cf")
    #     new_text = r.text.splitlines()
    #     for item in new_text:
    #         new_arr = str(item).split(':')
    #         arr.update({new_arr[0]:new_arr[1]})
	    
    #     return arr


    #     options = Options()

    #     options.add_argument(f"--proxy-server=http://223.205.29.143:8080")

    #     driver = webdriver.Chrome(options=options)
    #     driver.get('https://whatmyuseragent.com/')
    #     time.sleep(10)
    #     driver.quit()