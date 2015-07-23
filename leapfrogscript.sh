echo "Hello, world!"

virtualenv --no-site-packages selenium_project/

cd selenium_project/

source bin/activate

py.test leapfrog.py leapfrog.py
