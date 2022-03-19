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
            
    