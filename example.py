import time
from PIL import Image
from slider import slider_cracker
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains



'''chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(executable_path='chromedriver.exe',
    chrome_options=chrome_options)'''#Chrome无头模式
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://passport.bilibili.com/login')
time.sleep(1)

cracker = slider_cracker(driver)
cracker.crack()





