#import selenium libraries
from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the Selenium web driver (make sure you have the appropriate web driver for your browser installed)
driver = webdriver.Chrome()  # Change to the appropriate web driver for your browser

# Navigate to the webpage
driver.get("https://www.facebook.com/")

# Find the login form elements using their HTML attributes (you may need to adjust this based on the actual webpage structure)
username_input = driver.find_element(By.XPATH,'//*[@id="email"]')
password_input = driver.find_element(By.XPATH,'//*[@id="pass"]')
login_button = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button')

# Fill in the login form
username_input.send_keys("8424909579")
password_input.send_keys("8424918381")

# Submit the login form
login_button.click()

# Wait for the page to load after logging in (you may need to adjust the waiting time based on the webpage)
driver.implicitly_wait(10)

#Maximize the size of window
driver.maximize_window()


# To Close the browser
#driver.quit()
