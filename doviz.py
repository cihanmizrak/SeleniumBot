import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image

options = webdriver.ChromeOptions()
options.headless = True 
driver = webdriver.Chrome(options=options)

URL = "https://canlidoviz.com/yaani/"

driver.get(URL)

S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(S('Width'),S('Height'))       
path = str(datetime.now().date())                                                                                                        
driver.save_screenshot(f'{path}.png')

driver.quit()
im = Image.open(path + ".png")
im.show()
