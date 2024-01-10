from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

browser = webdriver.Chrome()
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)
    
    
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
 
    
    button = browser.find_element(By.CSS_SELECTOR, "#book.btn.btn-primary").click()
    
    x = browser.find_element(By.ID, "input_value").text
    result = calc(x)
    
    field = browser.find_element(By.ID, "answer").send_keys(result)
    button2 = browser.find_element(By.ID, "solve").click()
    
    alert_window = browser.switch_to.alert.text
    print(alert_window)
    
finally:
    time.sleep(2)
    browser.quit()
        