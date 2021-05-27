from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup as soup


class my_car:
    def __init__(self):
        self.base_url = "https://www.bilbasen.dk/"
        self.car_list = []
        
        print("Starting up...")
        
        profile = webdriver.FirefoxProfile()
        profile.set_preference("general.useragent.override", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0")
        options = Options()
        options.headless = True
        
        #Windows
        self.browser = webdriver.Firefox(options=options)
        
        #M1 
        #self.browser  = webdriver.Chrome(executable_path="/Users/frederikdahl/chromedriver/chromedriver")
        
        self.browser.get(self.base_url)
        print("Got Browser")
        
        self.browser.implicitly_wait(3)
        
    def click_cookie_button(self):
        try:
            cookie_button = self.browser.find_element_by_id('onetrust-accept-btn-handler')
            try:
                cookie_button.click()
                print("Cookie Button Clicked")
                sleep(3)   
            except Exception as err:
                print('Error With Cookie Button:', err)
        except Exception as err:
            print(err)
            
    def click_leasing_button(self):
        try:
            leasing_button = self.browser.find_element_by_css_selector("label[data-track-action='leasing-toggle']")
            try:
                leasing_button.click()
                print("Leasing Button Clicked")
                sleep(3)   
            except Exception as err:
                print('Error With Leasing Button:', err)
        except Exception as err:
            print(err)
        
    def search_in_search_bar(self, search_text):
        try:
            search_field = self.browser.find_element_by_class_name('react-autosuggest__input')
            search_field.send_keys(search_text)
            search_field.submit()
            print("Search Bar Entered")
            sleep(3)

        except Exception as err:
            print('Error with Search', err)

    def get_car_list(self):
        print("Souping Site")
        print()
        page_source = self.browser.page_source
        page_soup = soup(page_source,'html.parser')
        car_list_plus = page_soup.findAll("div",{"class":"row listing listing-plus bb-listing-clickable"})
        car_list_discount = page_soup.findAll("div",{"class":"row listing listing-discount bb-listing-clickable"})
        full_list = car_list_plus + car_list_discount
        print("Cars found: " + str(len(full_list)))
        for car in full_list:
            name = car.find("a",{"class":"listing-heading darkLink"}).contents[0]
            km = int(car.findAll("div",{"class":"col-xs-2 listing-data"})[1].contents[0].replace('.',''))
            price = car.find("div",{"class":"col-xs-3 listing-price"}).contents[0].replace(' kr.','').replace('.','')
            year = int(car.findAll("div",{"class":"col-xs-2 listing-data"})[2].contents[0])
            car_info = {"name": name, "km": km, "price": price, "year": year}
            self.car_list.append(car_info)
            print(car_info) 
            
    def close_browser(self):
        self.browser.close()