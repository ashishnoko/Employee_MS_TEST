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
    
    #Click to the paid leave
    
    paid_card =  wait.until(EC.element_to_be_clickable((By.XPATH,'(//div[@class="mt-9 bg-white"])[1]'))).click()
    time.sleep(4)
    
    #click on the New Leave
    
    newleave_click = wait.until(EC.element_to_be_clickable((By.XPATH,'(//div[@class="nav-wrapper"]//span[@class="py-4"])[1]'))).click()
    time.sleep(4)
    
    #enter the leave type
    
    leave_type = wait.until(EC.element_to_be_clickable((By.XPATH,'//select[@id="leave-type"]'))).click()
    time.sleep(2)
    select_leave = wait.until(EC.element_to_be_clickable((By.XPATH,'//option[@value="full_day"]'))).click()
    
    select_from_date = wait.until(EC.element_to_be_clickable((By.XPATH,'//input[@id="from-date"]'))).click()
    time.sleep(5)
    
    to_date = wait.until(EC.element_to_be_clickable((By.XPATH,'//input[@id="to-date"]'))).click()
    time.sleep(5)
    
    write_reason = wait.until(EC.element_to_be_clickable((By.XPATH,'//textarea[@rows="5"]'))).click()
    write_reason.send_keys("i want leave request")
    time.sleep(5)
    
    submit =  wait.until(EC.element_to_be_clickable((By.XPATH,'//textarea[@rows="5"]'))).click()
    
    
    

    
    
    

    
    
    

    
    
    
    
    
    teardown(driver)
    
log_in()
    
