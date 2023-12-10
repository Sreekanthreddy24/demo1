import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path='C:/Users/gansreek/Downloads/chromedriver-win64 (1)/chromedriver-win64/chromedriver.exe')
driver.maximize_window()
driver.get('https://www.amazon.com/')
time.sleep(8)
today_deals_link = driver.find_element_by_xpath("//img[@alt='Tineco Cordless Wet Dry Vacuum Cleaners']")
today_deals_link.click()
driver.implicitly_wait(5)
product_names = driver.find_elements_by_xpath("//div[@class='a-section octopus-dlp-asin-title']")
print("Today's Hot Deals:")
for product_name in product_names:
    print(product_name.text)

#     hifabvd
