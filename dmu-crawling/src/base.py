import time
from abc import ABC, abstractmethod

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CrawlerBase(ABC):
    def __init__(self, driver, root_url):
        self.driver = driver
        self.root_url = root_url
        
        super(CrawlerBase, self).__init__()
        
    @abstractmethod
    def move_to_root(self, indicator):
        pass

    
    def close_driver(self):
        self.driver.close()
        self.driver.quit()
        print(('='*5 + 'Driver Closed' + '='*5))