
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import requests
from bs4 import BeautifulSoup as bs
from selenium.webdriver import ActionChains as ac
import time
url3=''
url='https://www.booking.com/index.en-gb.html?label=gen173nr-1DCAEoggI46AdIM1gEaGyIAQGYAQm4ARfIAQzYAQPoAQGIAgGoAgO4AufO5pYGwAIB0gIkOGFmNjEyNmEtYjZlNS00ZWZmLThjZDktYjNhYzVjNzI5ZmJk2AIE4AIB&sid=9c69aa3c373490111ae3fec1935701bc&keep_landing=1&sb_price_type=total&'
url2='https://www.booking.com/searchresults.en-gb.html?label=gen173nr-1BCAEoggI46AdIM1gEaGyIAQGYAQm4ARfIAQzYAQHoAQGIAgGoAgO4AufO5pYGwAIB0gIkOGFmNjEyNmEtYjZlNS00ZWZmLThjZDktYjNhYzVjNzI5ZmJk2AIF4AIB&sid=df5ff50c5544ff8d93766c30fe2c4ea7&sb=1&sb_lp=1&src=index&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Findex.en-gb.html%3Flabel%3Dgen173nr-1BCAEoggI46AdIM1gEaGyIAQGYAQm4ARfIAQzYAQHoAQGIAgGoAgO4AufO5pYGwAIB0gIkOGFmNjEyNmEtYjZlNS00ZWZmLThjZDktYjNhYzVjNzI5ZmJk2AIF4AIB%26sid%3Ddf5ff50c5544ff8d93766c30fe2c4ea7%26sb_price_type%3Dtotal%26%26&ss=New+Delhi%2C+Delhi+NCR%2C+India&is_ski_area=&checkin_year=2022&checkin_month=8&checkin_monthday=24&checkout_year=2022&checkout_month=8&checkout_monthday=26&group_adults=4&group_children=0&no_rooms=2&b_h4u_keep_filters=&from_sf=1&ss_raw=delhi&ac_position=0&ac_langcode=en&ac_click_type=b&dest_id=-2106102&dest_type=city&iata=DEL&place_id_lat=28.6349&place_id_lon=77.2226&search_pageview_id=312e556d8498023f&search_selected=true&search_pageview_id=312e556d8498023f&ac_suggestion_list_length=5&ac_suggestion_theme_list_length=0'
class Booking(webdriver.Chrome):
    def __init__(self,teardown=False,wait=15):
        super().__init__()
        os.environ['PATH']+='C:\SeleniumDrivers'
        self.teardown=teardown
        self.implicitly_wait(wait)
        self.maximize_window()
    def __exit__(self,exc_type,exc_value,exc_traceback):
        if self.teardown:
            self.quit()
    def runsite(self):
        self.get(url)
    def location(self,place):
            f1=self.find_element(By.ID,'ss')
            f1.send_keys(place)
            print("selecting.....")
            f2=self.find_element(By.CSS_SELECTOR,'li[data-i="0"]')
            f2.click()
    def date(self,checkin,checkout):
        f1=self.find_element(By.CSS_SELECTOR,f'td[data-date="{checkin}"]')
        f1.click()
        f2 = self.find_element(By.CSS_SELECTOR, f'td[data-date="{checkout}"]')
        f2.click()
    def guests(self,adult=2,room=1):
        f1=self.find_element(By.ID,"xp__guests__toggle")
        f1.click()
        adult=adult-2
        room=room-1
        if adult<0:
            f1=self.find_element(By.CSS_SELECTOR,'button[aria-label="Decrease number of Adults"]')
            f1.click()
        else:
            f1 = self.find_element(By.CSS_SELECTOR, 'button[aria-label="Increase number of Adults"]')
            while adult:
                f1.click()
                adult-=1
        f1 = self.find_element(By.CSS_SELECTOR, 'button[aria-label="Increase number of Rooms"]')
        while room:
            f1.click()
            room-=1
        f2=self.find_element(By.CLASS_NAME,"sb-searchbox__button")
        f2.click()
    def price(self,low=0,high=3000):
        f1=self.find_element(By.ID,'filter-style-switch-pri')
        f1.click()
        f1=self.find_element(By.XPATH,'//input[@aria-label="Min."]')
        f2=self.find_element(By.CLASS_NAME,"cc235030af b3ebef74ed")
        ac(self).click_and_hold(f1).pause(1).move_by_offset(50, 0).release().perform()
        time.sleep(10)
        ac(self).move_to_element(f2).pause(1).click_and_hold().pause(1).move_by_offset(-100, 0).release().perform()
    def sort(self):
        self.find_element(By.CSS_SELECTOR, 'button[data-testid="sorters-dropdown-trigger"]').click()
        time.sleep(5)
        self.find_element(By.CSS_SELECTOR, 'button[data-id="price"]').click()
        h_t=requests.get(self.current_url).content
        soup=bs(h_t,'lxml')
        lis1=soup.find_all('div',class_="fcab3ed991 a23c043802")
        for i,sub in lis1:
            print(sub.text)
            if i==20:
                break




























