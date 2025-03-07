from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://namespace-team.github.io/ems-web/login")
    return driver

def teardown(driver):
    
    driver.quit()
    
def log_in():
    driver = setup()
    wait = WebDriverWait(driver,10)
    
    email_address = driver.find_element(By.XPATH,'//input[@id="username"]')
    email_address.send_keys('testuser@namespace.jp')
    
    password = driver.find_element(By.XPATH,'//input[@id="password"]')
    password.send_keys('p@ssw0rD44')

    signin_btn = wait.until(EC.element_to_be_clickable((By.XPATH,'//button')))
    signin_btn.click()
    time.sleep(4)
    
    #entering dashboard
    
    click_card=  wait.until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="mt-9 bg-white"]')))
    for i in range(len(click_card)):
        
        card=  wait.until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="mt-9 bg-white"]')))
        card[i].click()
        time.sleep(3)
        
        try:
            
            redirect_dashboard = wait.until(EC.element_to_be_clickable((By.XPATH,'(//a[@class="flex items-center"])[1]')))
            redirect_dashboard.click()
            time.sleep(5)
            
        except Exception as e:
            print(f"Error: {e}")
        
        
    
    
    
    
    
    teardown(driver)

log_in()

    