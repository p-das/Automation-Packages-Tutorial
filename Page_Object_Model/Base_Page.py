
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:

    def __init__(self,driver,waittime):
        self.driver= driver
        print("Initiated driver")
        self.waittime = waittime

    def element_locator(self,locator):
        ele = WebDriverWait(self.driver, self.waittime).until(EC.element_to_be_clickable((By.XPATH, locator)),
                                             message=f"Unable to locate element {locator}")
        return ele

