# import selenium webdriver module  to launch and control the web browsers
# import ActionChains, a Selenium class used to simulate complex user actions
# import the By class for locating web elements
# import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

# set driver to chrom
# get jquery website
driver = webdriver.Chrome()
driver.get("https://jqueryui.com/droppable/")

# driver to find css selector,source and target by id
driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR,".demo-frame"))
source = driver.find_element(By.ID, "draggable")
target = driver.find_element(By.ID, "droppable")
# call action chain method
action = ActionChains(driver)

# use  various methods of action chain
# drag and drop offset holds down the left mouse button on the source element, then moves to the target offset and releases the mouse button
action.drag_and_drop_by_offset(source,150,30).perform()

# click and holds down the left mouse button on an element.
action.click_and_hold(source)

# Moving the mouse to the middle of an element
action .move_to_element(target)

# Releasing a held mouse button on an element
action.release()

# Performs all stored actions
action.perform()

# Holds down the left mouse button on the source element, then moves to the target element and releases the mouse button
action.drag_and_drop(source,target).perform()
time.sleep(5)
driver.quit()


