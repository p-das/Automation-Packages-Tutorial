import sys
sys.path.insert(0,r'Automation_Framework_Tutorial\Object_Repository')
sys.path.insert(0,r'Automation_Framework_Tutorial\Page_Object_Model')
from Object_Repository import objectrepository_imdb as OR
from Page_Object_Model.Base_Page import BasePage

class SignIN(BasePage):

    def fn_verify_title(self):
        '''Verifying title of 1st page'''
        browser_title = self.driver.title
        icon_element = self.element_locator(OR.imdb_icon_xpath)
        if browser_title == 'IMDb: Ratings, Reviews, and Where to Watch the Best Movies & TV Shows' and icon_element.is_displayed():
            print("Opened correct URL. IMDB Icon is displaying")
            status = 'Passed'
        else:
            status = 'FAILED'
            print(f"Unable to open URL.Browser Title in actual:{browser_title}.")
        return status

    def fn_login(self, user_id, password,role):
        try:
            '''Sign in'''
            sign_in_ele = self.element_locator(OR.sign_in_xpath)
            if sign_in_ele.is_displayed():
                print("Sign in button visible")
                sign_in_ele.click()
                sign_in_imdb_ele = self.element_locator(OR.sign_in_wt_imdb_xpath)
                sign_in_imdb_ele.click()
                print("Clicked on Sign in with IMDB")
                email_ele = self.element_locator(OR.email_input_xpath)
                email_ele.send_keys(user_id)
                pswd_ele = self.element_locator(OR.pswd_input_xpath)
                pswd_ele.send_keys(password)
                sign_in_btn_ele = self.element_locator(OR.sign_in_button_xpath)
                sign_in_btn_ele.click()
                print("Clicked on Sign in button")
                role_ele = self.element_locator(OR.role_text_xpath)
                role_name = role_ele.text
                print("Role Name is:", role_name)
                if role == role_name:
                    print("Login Successful")
                    status = 'Passed'
                else:
                    print(f"Login unsuccessful. Role in application:{role_name}")
                    status = 'Failed'
            else:
                print(f"Login unsuccessful. Sign In element is not displaying")
                status = 'Failed'
        except Exception as e:
            print(f"Login unsuccessful. Error:{e}")
            status = 'Failed'
        return status