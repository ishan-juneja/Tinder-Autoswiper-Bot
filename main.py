import undetected_chromedriver as uc #https://stackoverflow.com/questions/59515561/this-browser-or-app-may-not-be-secure-error-while-attempting-to-login-in-to-gm
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time
import os
from pyotp import * #https://stackoverflow.com/questions/55870489/how-to-handle-google-authenticator-with-selenium, https://letzdotesting.com/how-to-automate-two-factor-authentication-with-google-authenticator-using-selenium/
from selenium.webdriver.remote.webelement import WebElement

tinder_email = os.environ["TINDER_EMAIL"]
tinder_password = os.environ["TINDER_PASSWORD"]
NUMBER_OF_SWIPES = 3
SHORT_WAIT = 1.5
MEDIUM_WAIT = 5
LONG_WAIT = 15

chrome_driver_path = "/Users/ishanjuneja/Development/chromedriver_mac64"

tinder_path = "https://tinder.com/"

service = Service(chrome_driver_path)
driver = uc.Chrome()
driver.get(tinder_path)

#LOGIN STEPS
time.sleep(SHORT_WAIT)
buttons = driver.find_elements(By.CLASS_NAME, "l17p5q9z")
for button in buttons:
	time.sleep(SHORT_WAIT)
	if(button.text == "Log in"):
		button.click()
		break

time.sleep(SHORT_WAIT)

#entering in through google
# ATTENTION: I was trying to automatically click the login through google button yet was unable to
# hence why over here you see me sleeping for 5 seconds only which is where the user is supposed to
# click the button themselves
# Provide tinder our location privelages --> this is required to use tinder

time.sleep(MEDIUM_WAIT)
#changing window to the google email one
g_login_window = driver.window_handles[1]
driver.switch_to.window(g_login_window)
print(driver.title)

#logging in to our email
time.sleep(SHORT_WAIT)
email_field = driver.find_element(By.CLASS_NAME, "whsOnd")
email_field.send_keys(tinder_email + Keys.RETURN)

time.sleep(SHORT_WAIT)
password_field = driver.find_element(By.CLASS_NAME, "whsOnd")
password_field.send_keys(tinder_password + Keys.RETURN)

# ATTENTION: UNCOMMENT THIS OUT IF GOOGLE IS LETTING YOU USE YOUR PHONE CONFIRMATION
time.sleep(SHORT_WAIT)
try_another_way_link = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div[2]/div[2]/div/div/button")
try_another_way_link.click()

time.sleep(MEDIUM_WAIT)
google_authenticator: WebElement = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section[2]/div/div/section/div/div/div/ul/li[2]/div")
google_authenticator.click()

#bypasS 2FA using totp
time.sleep(SHORT_WAIT)
totp = TOTP("t44h6rcqywooo4wnttvdxlqp6waqvebn")
token = totp.now()
code_field = driver.find_element(By.CLASS_NAME, "whsOnd")
code_field.send_keys(token + Keys.RETURN)

time.sleep(MEDIUM_WAIT)

#switching back to working in tinder
tinder_window = driver.window_handles[0]
driver.switch_to.window(tinder_window)
print(driver.title)



#Surpassing the location button
location_button = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[1]/div/div/div[3]/button[1]")
location_button.click()
#ATTENTION: This is the second place where a manual click is required where chrome may ask you to share your location

#Declining to get notifications
time.sleep(MEDIUM_WAIT)
notification_decline_button = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[1]/div/div/div[3]/button[2]/div[2]/div[2]")
notification_decline_button.click()

#Swiping right on every person
driver.refresh()
for i in range (0, NUMBER_OF_SWIPES):
	try:
		time.sleep(MEDIUM_WAIT)
		print("hi")
		like_button = driver.find_element(By.XPATH,
		                                  "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[4]/button")

		driver.execute_script("arguments[0].click();", like_button)

	except NoSuchElementException:
		try:
			time.sleep(MEDIUM_WAIT)
			print("hi2")
			like_button = driver.find_element(By.XPATH,
			                                  "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button")

			driver.execute_script("arguments[0].click();", like_button)
		except NoSuchElementException:
			time.sleep(MEDIUM_WAIT)
			match_exit = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/main/div/div[1]/div/div[4]/button")
			driver.execute_script("arguments[0].click();", match_exit)

while(True):
	pass