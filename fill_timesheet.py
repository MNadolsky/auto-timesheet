
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By as by
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from datetime import date, datetime, timedelta



driver = webdriver.Chrome()
driver.implicitly_wait(20)

url = os.environ.get('TIMESHEET_URL')
username = os.environ.get('TIMESHEET_USERNAME')
password = os.environ.get('TIMESHEET_PASSWORD')

# log in

driver.get(url)
driver.find_element(by.ID, 'username').send_keys(username)
driver.find_element(by.ID, 'password').send_keys(password)
driver.find_element(by.TAG_NAME, 'button').click()

# access timesheet

driver.find_element(by.XPATH, '//a[text()="My Timesheet - Modern"]').click()
driver.switch_to.window(driver.window_handles[1]) #switch tabs
wait(driver,20).until(EC.presence_of_element_located((by.XPATH, '//table[contains(@class, "table")]')))

# find this week

def get_week():
    time.sleep(2)
    week_link = driver.find_element(by.XPATH, '//ul[@class="timesheet-carousel"]/li[2]/div') # center item
    # you are the weekest link
    week_metadata = week_link.find_elements(by.XPATH, './/div')
    week = week_metadata[0].text
    week_start = datetime.strptime(week.split('-')[0] + str(datetime.today().year), '%b %d %Y')
    week_end   = datetime.strptime(week.split('-')[1].strip() + ' ' + str(datetime.today().year), '%b %d %Y')
    status = week_metadata[1].text
    return week_link, week_start, week_end, status

week_link, week_start, week_end, status = get_week()
while datetime.today() < week_start:
    driver.find_element(by.XPATH, '//div[@class="control-left"]/*').click()
    time.sleep(1)
    week_link, week_start, week_end, status = get_week()
while datetime.today() > week_end:
    driver.find_element(by.XPATH, '//div[@class="control-right"]/*').click()
    time.sleep(1)
    week_link, week_start, week_end, status = get_week()

# fill out timesheet

if status == 'Open':
    week_link.click()
    driver.find_element(by.XPATH, '//button[@data-caid="add-work-button"]').click()
    driver.find_element(by.XPATH, '//li[./a/ppm-multiline-ellipsis = "Copy Previous Timesheet (with time)"]').click()
    driver.find_element(by.XPATH, '//button[@aria-label="Submit & attest"]').click()

# cleanup

time.sleep(10)
driver.quit()
