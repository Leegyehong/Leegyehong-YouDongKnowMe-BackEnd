import sys
sys.path.append('.')
import os
import time
import datetime
import json
import argparse
from pathlib import Path
from utils.utils import read_config
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from dataclasses import dataclass

from src.noti import NotiCrawler

import pandas as pd
from sqlalchemy import create_engine 
from tabulate import tabulate
#from utils.drivers.unzipper import InstallDriver


@dataclass
class Config:
    def __init__(self, config_dict):
        self.root_url = config_dict['root_url']
        self.indicator = config_dict['major_name']
        self.major_code = config_dict['major_code']
        if self.indicator is not None:
            self.log_dir_name = f'{config_dict["data_dir"]}\\crawlled\\'+ datetime.datetime.now().strftime('%Y-%m-%d') + f'\\{self.indicator}'
        
        self.create_dir()
    
    def create_dir(self):
        Path(self.log_dir_name).mkdir(exist_ok=True, parents=True)
        
    def config_info(self):
        return {
                'url' : self.root_url,
                'major_name' : self.indicator
                }


def get_driver():
    options = Options()
    options.headless = False
    options.add_experimental_option('detach', True)
    options.add_argument('--no-sandbox')
    options.add_argument('--incognito')
    options.add_argument('--disable-setuid-sandbox')
    options.add_argument('--disable-dev-shm-usage')
        
    driver = Chrome(ChromeDriverManager().install(), options=options)
    
    return driver

def initate_crawler(driver,
                    config,
                    root_url):
    
    crawler = NotiCrawler(driver = driver, 
                        root_url = root_url)
    
    return crawler
    
def main(config):
    print(f'Starting Crwaler {config.root_url}\t{config.indicator}')
    driver = get_driver()
    crawler = initate_crawler(driver=driver, 
                            config=config,
                            root_url=config.root_url)
    crawler.get_data(config)
    crawler.close_driver()
    
    
    
if __name__ =='__main__':
    #InstallDriver()
    parser = argparse.ArgumentParser()
    parser.add_argument('--config_path',
                        type=str,
                        default='dmu-crawling\\config\\dmu\\test\\dmu_컴퓨터공학부_컴소과_공지사항.yaml',
                        help='target config yaml file path')
    args = parser.parse_args()

    config = Config(read_config(args.config_path))
    
    main(config)