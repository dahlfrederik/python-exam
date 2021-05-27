from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup as soup
import re


class numberplate_scraper:
    def __init__(self,nummerplade, windows):
        
        print("Starting up..")
        profile = webdriver.FirefoxProfile()
        profile.set_preference("general.useragent.override", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0")
        options = Options()
        options.headless = True

        # Windows
        if(windows == True):
            self.browser = webdriver.Firefox(options=options)
            # M1
        else:
            self.browser = webdriver.Chrome(executable_path="/Users/frederikdahl/chromedriver/chromedriver")

        self.browser.get("https://www.nummerplade.net/")

        print("Got Browser")

        self.browser.implicitly_wait(3)

        search_field = self.browser.find_element_by_id('search_regnr')

        search_field.send_keys(nummerplade)
        #search_field.send_keys("CM 58 541")

        button = self.browser.find_element_by_id('search_regnr_button')
        button.click()
        print("Search Entered")
        sleep(3)

        print("Search done")
    
    def get_car_make_model(self):
        page_source = self.browser.page_source
        page_soup = soup(page_source,'html.parser')
        res = page_soup.select_one("#maerke").text +" "+ page_soup.select_one("#model").text + " "
        return res


    def get_car_km(self):
        page_source = self.browser.page_source
        page_soup = soup(page_source,'html.parser')
        search_car_km = page_soup.select_one("#box-overblik-data-overblik_kmcheck > div > small").text + " "
        filter_search_km = re.sub("[^0-9]+", "",search_car_km)
        search_car_km = filter_search_km
        return search_car_km


    def get_car_model_year(self):
        page_source = self.browser.page_source
        page_soup = soup(page_source,'html.parser')
        search_car_year = page_soup.select_one("#model_aar").text +" " 
        return search_car_year


    def close_browser(self):
        self.browser.quit()