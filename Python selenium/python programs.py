# This is selenium 4 version
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
service = Service(executable_path='C:/Users/gansreek/Downloads/chromedriver-win64 (1)/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(options=options, service=service)

driver.maximize_window()
driver.get('https://www.amazon.in/')
a = driver.find_element(By.ID,("twotabsearchtextbox"))
a.click()
a.send_keys('iphone 14')
b = driver.find_element(By.ID,("nav-search-submit-button"))
b.click()
# c = driver.find_element(By.XPATH,('//*[@id="CardInstancemJYwYf1TWT6UP4RPVWTE3g"]/div[1]/div[1]/div[2]/div/div[1]/div[2]/div[1]/a/div/img'))
# c.click()
driver.find_element(By.XPATH,'(//span[@class="a-size-medium a-color-base a-text-normal"])[1]').click()


#
# driver.find_element(By.XPATH,'//input[@type="text"]').send_keys('iphone')
# driver.find_element(By.XPATH,'//input[@id="nav-search-submit-button"]').click()
# phone = driver.find_elements(By.XPATH,'//span[@class="a-size-medium a-color-base a-text-normal"]')
# for i in phone:
#     print(i.text)
#     if i.text == 'Apple iPhone 12 (128GB) - Green':
#         i.click()
# #parent = driver.window_handles[1]
# #driver.switch_to.window(parent)
# driver.switch_to.window(driver.window_handles[1])
# print(driver.title)
# print(driver.find_element(By.XPATH,'//table[@class="a-normal a-spacing-micro"]').text)
# phone_details_in_list = driver.find_elements(By.XPATH,'//span[@class="a-size-base a-text-bold"]')
# print(phone_details_in_list)
# time.sleep(2)
# # driver.quit()
