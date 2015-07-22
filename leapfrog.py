# browser = webdriver.Firefox()
# browser.get('http://seleniumhq.org/')

# driver.get("http://www.google.com")
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

    # the page is ajaxy so the title is originally this:
    # print driver.title

    # find the element that's name attribute is q (the google search box)
    inputElement = driver.find_element_by_name("q")

    # type in the search
    inputElement.send_keys("fish food")

    # submit the form (although google automatically searches now without submitting)
    inputElement.submit()



    # wiki = driver.find_elements_by_xpath("//*[contains(text(), 'wikipedia')]")
    #
    # wiki.click()

    # try:
    #     # we have to wait for the page to refresh, the last thing that seems to be updated is the title
    WebDriverWait(driver, 110).until(EC.title_contains("fish food"))

    #
    #     # You should see "cheese! - Google Search"
    # print driver.title

    # wiki = driver.find_elements_by_xpath("id('rso')/x:div[3]/x:li[1]/x:div/x:h3/x:a")

    # that's firefox, google's is //*[@id="rso"]/div[3]/li[1]/div/h3/a

    wiki = driver.find_element_by_xpath("//*[contains(text(), 'Wikipedia')]")

    wiki.click()

    heading = driver.find_element_by_id("firstHeading")

    collapse = driver.find_element_by_id("collapseButton0")

    collapse.click()

    # if "Aquarium fish feed" in heading.text:
    #     raise Exception("pass")

    if not "Aquatic fish feed" in heading.text:
        raise Exception("Switch Aquatic to Aquarium to pass the test")

    driver.quit

    # heading
    #
    # finally:
    #     driver.quit()
    #get value from title tag
    # assert means check if title
