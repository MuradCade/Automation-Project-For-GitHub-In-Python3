from selenium import webdriver
import time


#asking for the name of the reposotory and the description that the reposotory will require

repository = input("Enter The Name Of The Reposotory: ")
description= input("Enter The Description Of The Reposotory: ")




driver = webdriver.Chrome()

driver.get('https://github.com/login')

# I Use Execute_Script To Scroll Through The Page

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# In Here Put Your Email That Yo Register In Github

user1 = driver.find_element_by_xpath('//*[@id="login_field"]')
user1.send_keys('Email_Require')

#In Here Enter The Password Of The Email That You Enter
pas = driver.find_element_by_xpath('//*[@id="password"]')
pas.send_keys('Password_Require')

signbt = driver.find_element_by_xpath('//*[@id="login"]/div[4]/form/input[14]')
signbt.click()

butt = driver.find_element_by_xpath('/html/body/div[1]/header/div[7]/details/summary/span[2]')
butt.click()

time.sleep(2)

butt1 = driver.find_element_by_xpath('/html/body/div[1]/header/div[7]/details/details-menu/a[1]')
butt1.click()



btt2 = driver.find_element_by_xpath('/html/body/div[1]/header/div[6]/details/summary/span')
btt2.click()

btt3  = driver.find_element_by_xpath('/html/body/div[1]/header/div[6]/details/details-menu/a[1]')
btt3.click()


textbox = driver.find_element_by_name('repository[name]')
textbox.send_keys(repository)


textbox1 = driver.find_element_by_name('repository[description]')
textbox1.send_keys(description)


driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


time.sleep(2)
selbox = driver.find_element_by_xpath('/html/body/div[4]/main/div/form/div[4]/div[4]/div[1]/label/input[2]').click()


lsit = driver.find_element_by_xpath('//*[@id="new_repository"]/div[4]/button')
lsit.click()
