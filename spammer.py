from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

print('Python code for automating discord messages.')
driver = webdriver.Chrome()
server = input('Input the url for the channel of your choice: ')

driver.get(server)
usemail = input('Input email: ')
uspassword = input('Password: ')

email = driver.find_element_by_name('email')
email.send_keys(usemail)
password = driver.find_element_by_name('password')
password.send_keys(uspassword)
buttons = driver.find_elements_by_tag_name('button')
buttons[1].click()

message = input('What message would you like to spam? ')

print('Initializing...')
time.sleep(10)
print('Starting...')

while True:  
    actions = ActionChains(driver)
    actions.send_keys(message, Keys.RETURN)
    actions.perform()
    time.sleep(60)