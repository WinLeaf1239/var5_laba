#pip install undetected-chromedriver

#pip install setuptools

#https://googlechromelabs.github.io/chrome-for-testing/#stable

import requests
import time
import selenium
import os
import random
from PIL import Image , ImageEnhance
import undetected_chromedriver as uc 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pandas as pd



class Parcer():

    def __init__(self, link, klas):
        self.link = link
        self.klas = klas
        desktop_path = os.path.join(os.environ['USERPROFILE'], 'Desktop')
        chrome_156_path = os.path.join(desktop_path, 'Chrome156', 'chrome.exe')
        if not os.path.exists(chrome_156_path):
            raise FileNotFoundError(f"Не удалось найти Chrome по пути: {chrome_156_path}. Проверьте имя папки.")

        options = uc.ChromeOptions()

        self.driver = uc.Chrome(options=options, browser_executable_path=chrome_156_path)
        self.driver.get(self.link)


        # self.driver = webdriver.Chrome()
        # self.driver.get(self.link)
        time.sleep(10)


    def getlinks(self):

#БЛОК ИИ
        print("Начинаю плавный скролл страницы для подгрузки всех товаров...")
        
        # Задаем шаг прокрутки в пикселях и задержку между шагами
        scroll_step = 400  
        scroll_delay = 0.3  # секунды
        
        # Получаем полную высоту страницы на старте
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        current_position = 0

        while True:
            # Скроллим на фиксированный шаг вниз
            current_position += scroll_step
            self.driver.execute_script(f"window.scrollTo(0, {current_position});")
            time.sleep(scroll_delay)
            
            # Раз в несколько шагов проверяем, не дошли ли мы до самого конца страницы
            if current_position % 2000 == 0:
                new_height = self.driver.execute_script("return document.body.scrollHeight")
                # Если мы пролистали ниже текущей высоты и она перестала расти — мы внизу
                if current_position >= new_height:
                    # На WB в самом низу может появиться пагинация или футер, 
                    # делаем финальную небольшую паузу на случай ленивой загрузки последних картинок
                    time.sleep(2)
                    break
#############################












        elements_first_page = self.driver.find_elements(By.CLASS_NAME, self.klas)
        links_list = []
        for element in elements_first_page:
            url = element.get_attribute('href')
            links_list.append(url)
        print(links_list)

    def __del__(self):
        self.driver.quit()

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