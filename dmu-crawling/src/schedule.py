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


class ScheduleCrawler(CrawlerBase):
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
        
        df = pd.DataFrame(columns=['month','date', 'content'])
        schedules = driver.find_elements_by_css_selector('.yearSchdulWrap')
        
        for i, schedule in enumerate(schedules,1):
            print(i, schedule)
            date_list = schedule.find_elements_by_tag_name('dt')
            content_list = schedule.find_elements_by_tag_name('dd')
            for j in range(len(date_list)):
                df = df.append(pd.Series([i,date_list[j].text, content_list[j].text ], index=df.columns), ignore_index= True)
        
        
        df.to_csv(f'./crawled/{config.indicator}.csv', index=False)
        # data = pd.read_csv(f'./{config.indicator}.csv')
        # engine = create_engine("postgresql://postgres:postgres@localhost:5432/CrawledData", convert_unicode = False, connect_args={'connect_timeout': 3})
        # conn = engine.connect()
        # data.to_sql(name='noti',con = conn, if_exists='append')
        # conn.close()
