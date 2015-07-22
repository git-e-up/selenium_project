
import unittest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

def test_run():
    # Create a new instance of the Firefox driver
    driver = webdriver.Firefox()

    # go to the google home page
    driver.get("http://www.google.com")

    # find the element that's name attribute is q (the google search box)
    inputElement = driver.find_element_by_name("q")

    # type in the search
    inputElement.send_keys("fish food")

    # submit the form (although google automatically searches now without submitting)
    inputElement.submit()

    # we have to wait for the page to refresh, the last thing that seems to be updated is the title
    WebDriverWait(driver, 5000).until(EC.title_contains("fish food"))

    # find the Wikipedia link
    wiki = driver.find_element_by_xpath("//*[contains(text(), 'Wikipedia')]")

    # click the Wikipedia link
    wiki.click()

    # find the heading
    heading = driver.find_element_by_id("firstHeading")

    # find the hide button
    collapse = driver.find_element_by_id("collapseButton0")

    # click the hide button
    collapse.click()

    # Since the heading should be Aquarium and not Aquatic, this won't pass.
    if not "Aquatic fish feed" in heading.text:
        raise Exception("Switch Aquatic to Aquarium to pass the test")

    driver.quit
