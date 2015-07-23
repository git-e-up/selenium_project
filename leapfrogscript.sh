# echo "Hello, world!"

virtualenv --no-site-packages selenium_project/

# cd selenium_project/

source selenium_project/bin/activate

pip install requests

py.test leapfrog.py
