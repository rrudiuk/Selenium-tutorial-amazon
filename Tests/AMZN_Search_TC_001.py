import unittest
from selenium import webdriver

class AmazonHomePage(unittest.TestCase):
    # declare variable to store the URL to be visited
    base_url="https://www.amazon.in"

    # --- Pre - Condition ---
    def setUp(self):
        # disable gpu error in terminal
        chrome_opt = webdriver.ChromeOptions()
        chrome_opt.add_argument('--disable-gpu')
        # path to driver
        path = r"C:/drivers/chromedriver.exe"
        # declare and initialize driver variable
        self.driver = webdriver.Chrome(executable_path=path,chrome_options=chrome_opt)

        # browser should be loaded in maximized window
        self.driver.maximize_window()

        # driver should wait implicitly for a given duration, for the element under consideration to load.
        # to enforce this setting we will use builtin implicitly_wait() function of our 'driver' object.
        self.driver.implicitly_wait(10) #10 is in seconds

        # --- Steps ---
    def test_load_home_page(self):
        # to initialize a variable to hold reference of webdriver instance being passed to the function as a reference.
        driver=self.driver
        # to load a given URL in browser window
        driver.get(self.base_url)
        # test whether correct URL/ Web Site has been loaded or not
        self.assertIn("Amazon",driver.title)

    # --- Post - Condition ---
    def tearDown(self):
        # to close the browser
        self.driver.close()

if __name__ == "__main__":
    unittest.main()