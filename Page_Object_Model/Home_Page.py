
import sys
sys.path.insert(0,r'Automation_Framework_Tutorial\Object_Repository')
sys.path.insert(0,r'Automation_Framework_Tutorial\Page_Object_Model')
from Page_Object_Model.Base_Page import BasePage
from Object_Repository import objectrepository_imdb as OR

class Home(BasePage):

    def fn_logout(self):
        try:
            '''Sign Out'''
            acnt_ele = self.element_locator(OR.account_xpath)
            acnt_ele.click()
            sign_out_ele = self.element_locator(OR.sign_out_xpath)
            sign_out_ele.click()
            sign_in_ele = self.element_locator(OR.sign_in_xpath)
            print("Clicked on Account dropdown")
            if sign_in_ele.is_displayed():
                print("Sign Out Successful")
                status = 'Passed'
            else:
                print("Sign Out Unuccessful")
                status='Failed'
        except Exception as e:
            print(f"Logout unsuccessful. Error:{e}")
            status = 'Failed'
        return status