import sys
sys.path.append('.')

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome

from src.base import CrawlerBase
from selenium.webdriver.chrome.options import Options
import os
import json
import datetime
from uuid import uuid4
import time
import pandas as pd

from sqlalchemy import create_engine 


class NotiCrawler(CrawlerBase):
    def __init__(self,
                driver,
                root_url,
                log_dir='data'):
        
        super().__init__(driver, root_url)
        self.driver = driver
        self.root_url = root_url
        self.log_dir = log_dir
        os.makedirs(self.log_dir, exist_ok=True)
        self.move_to_root()
        self.crawled_date = datetime.datetime.now().strftime('%Y.%m.%d')
        self.crawler_id = str(uuid4())
        
    def move_to_root(self):
        try:
            self.driver.get(self.root_url)
            print(f'SUCCESS | Move to Root | {self.root_url}')
        except Exception as e:
            print(f'FAIL | Move to Root | {self.root_url}')
    
    def get_data(self, config):
        driver = self.driver
        
        df = pd.DataFrame(columns=['major_code', 'num', 'title' ,'writer', 'date', 'content', 'img_url','file_url'])
        while True:
            time.sleep(2)
            tr = driver.find_elements_by_css_selector('table > tbody > tr:not(.notice)')
            print('df size : ', len(df))
            if len(df) > 500:
                print('crawling End')
                break
            for i in range(len(tr)):
                tr = driver.find_elements_by_css_selector('table > tbody > tr:not(.notice)')
                print('meta crawling start')
                num = tr[i].find_element_by_css_selector('.td-num').text
                title = tr[i].find_element_by_css_selector('.td-subject').text
                writer = tr[i].find_element_by_css_selector('.td-write').text
                date = tr[i].find_element_by_css_selector('.td-date').text
                add_file = tr[i].find_element_by_css_selector('.td-file').text
                print(num, title, writer, date, add_file)
                print('meta crawling end')
                file_list = []
                time.sleep(1)
                tr[i].find_element_by_css_selector('.td-subject').click()
                time.sleep(1)
                print('content crawling start')
                
                content = driver.find_element_by_css_selector('div.view-con').text
                imgs = driver.find_elements_by_css_selector('div.view-con  img')
                img_url_list = []
                for img in imgs:
                    img_url_list.append(img.get_attribute('src'))
                if int(add_file)>0:
                    insert_file_url = driver.find_elements_by_css_selector(' div.view-file > dl > dd > ul > li a')
                    
                    for insert_url in insert_file_url:
                        file_url = insert_url.get_attribute('href')
                        file_title = insert_url.text
                        file_list.append({file_url:file_title})
                print('content crawling end')
                driver.back()
                time.sleep(1)
                df = df.append(pd.Series([config.major_code, num, title, writer, date, content, ' '.join(f for f in img_url_list) ,file_list], index=df.columns), ignore_index= True)
            
            time.sleep(1)
            
            pages = driver.find_elements_by_css_selector('form:nth-child(3) > div > div > ul >li')
            page_now = driver.find_element_by_css_selector('form:nth-child(3) > div > div > ul >li > strong')
            
            if int(pages[-1].text) == int(page_now.text):
                try:
                    driver.find_element_by_css_selector('form:nth-child(3) > div > div > a._next').click()
                except:
                    print("crawling End")
                    break
            else:
                for page in pages:
                    if int(page.text) == int(page_now.text)+1 :
                        page.click()
                        break
        
        
        df.to_csv(f'./crawled/{config.indicator}.csv', index=False)
        # data = pd.read_csv(f'./{config.indicator}.csv')
        # engine = create_engine("postgresql://postgres:postgres@localhost:5432/CrawledData", convert_unicode = False, connect_args={'connect_timeout': 3})
        # conn = engine.connect()
        # data.to_sql(name='noti',con = conn, if_exists='append')
        # conn.close()
