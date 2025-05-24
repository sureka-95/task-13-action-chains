# import the pytest testing framework to write and  a run test scripts
# import selenium webdriver module  to launch and control the web browsers
# import ActionChains, a Selenium class used to simulate complex user actions
# import the By class for locating web elements
# import WebDriverWait, a class used to create explicit waits
# import expected_conditions and gives it a short name EC
import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# EC is used with WebDriverWait to define what condition to wait for


# Used for setting up resources (like opening and closing a browser) that can be reused in multiple tests
# set up browser and get the jquery.com
@pytest.fixture
def setup_browser():
    driver = webdriver.Chrome()
    driver.get("https://jqueryui.com/droppable/")
    # wait for until the css.selector for demo-frame find
    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, ".demo-frame")))
    yield driver
    driver.quit()

# define the posituve test case function and using the setup fixture
def test_positive_drag_and_drop(setup_browser):
    driver = setup_browser
    # assingn the value for source and target
    source = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "draggable")))
    target = driver.find_element(By.ID, "droppable")
# use action chains to drag and drop and perform it
    ActionChains(driver).drag_and_drop(source, target).perform()

    # Assert statement used to verify  the text inside the target changes to Dropped
    result_text = target.text
    assert result_text == "Dropped!", f"Expected 'Dropped!' but got '{result_text}'"
    time.sleep(5)

# define negative test cases and use fixture init
def test_negative_drag_and_drop(setup_browser):
    driver = setup_browser
    # assign the value for source and target by id
    source = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "draggable")))
    target = driver.find_element(By.ID, "droppable")

    # Drag the element to a wrong place (not on the target)
    # use action chain drag and drop offset to perform to not place in the target
    ActionChains(driver).drag_and_drop_by_offset(source, -200, 0).perform()

    #  Assert statement used to  verify the text inside the target should remain "Drop here" or not
    result_text = target.text
    assert result_text == "Drop here", f"Expected 'Drop here' but got '{result_text}'"
    time.sleep(5)
# finally done and quit the browser and get the output