# selenium_project

This is a [Python Selenium WebDriver](https://pypi.python.org/pypi/selenium/2.46.1) test to determine whether the heading of a Wikipedia page matches the expected result (Hint: it doesn't pass). It also clicks the "hide" button in the purple section at the bottom of the page. 

It uses [virtualenv](https://pypi.python.org/pypi/virtualenv) to reproduce the environment in which it was built.

To run the test, clone the repo, switch into it, and run the following script:

`$ ./leapfrogscript.sh`

Requirements: Python 2.6, 2.7, 3.2, 3.3

Note: if your computer or internet connection are running slowly, the test may time-out and tell you the element isn't found. In that case just run the script again and it should work.
