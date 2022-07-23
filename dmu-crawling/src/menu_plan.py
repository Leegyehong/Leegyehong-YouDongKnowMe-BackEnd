from msilib.schema import Error
import sys
sys.path.append('.')

from datetime import date

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


class MenuPlanCrawler(CrawlerBase):
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
       # driver.get('https://www.dongyang.ac.kr/dongyang/130/subview.do')
        today = date.today()
        df = pd.DataFrame(columns=['range','date','restaurant' , 'menu_division', 'menu_content', 'etc_info'])
        
        
       # t_body[2//2].find_element_by_css_selector('th').text
       
        while True:
            t_body = driver.find_elements_by_css_selector('#viewForm > div > table > tbody > tr')
            time.sleep(2)
            range = driver.find_elements_by_xpath('//*[@id="_JW_diet_basic"]/div')[0].text.split('\n')[1]
            last_range = datetime.datetime.strptime(range.split('~ ')[1],"%Y.%m.%d").date()
            if today + datetime.timedelta(days=14) < last_range:
                break
            for i, el in enumerate(t_body):
                try:
                    date = t_body[i].find_element_by_css_selector('th').text
                except:
                    date = t_body[i-1].find_element_by_css_selector('th').text
                restaurant = t_body[i].find_elements_by_css_selector('td')[0].text
                menu_division = t_body[i].find_elements_by_css_selector('td')[1].text
                try:
                    menu_content = t_body[i].find_elements_by_css_selector('td')[2].text
                except:
                    menu_content = '-'
                try:
                    etc_info = t_body[i].find_elements_by_css_selector('td')[3].text
                except:
                    etc_info = '-'
                df = df.append(pd.Series([range, date, restaurant, menu_division, menu_content, etc_info], index=df.columns), ignore_index=True)
            driver.find_element_by_css_selector('#_JW_diet_basic > div > input._termRight').click()
        
        #df.to_csv(f'./crawled/{config.indicator}.csv', index=False)
        df.to_csv(f'./dmu-crawling/crawled/schedule/학교_학사일정.csv', index=False)
        # data = pd.read_csv(f'./{config.indicator}.csv')
        # engine = create_engine("postgresql://postgres:postgres@localhost:5432/CrawledData", convert_unicode = False, connect_args={'connect_timeout': 3})
        # conn = engine.connect()
        # data.to_sql(name='noti',con = conn, if_exists='append')
        # conn.close()
