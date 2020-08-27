from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_edit_and_save_cv(self):
        self.browser.get('http://localhost:8000')

        self.assertIn('Django Girls Blog', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text  
        self.assertIn('Django Girls Blog', header_text)

        goToCV = self.browser.get('http://localhost:8000/mycv')
        self.assertIn('Eni Segun CV', self.browser.find_element_by_class_name('cv_name').text)

        editbox = self.browser.find_element_by_id('id_edit_section')

        editbox.click()
        time.sleep(1)

        inputbox = self.browser.find_element_by_class_name('cv-form')
        
        actions = ActionChains(self.browser)
        actions.click(inputbox)
        actions.key_down(Keys.COMMAND).send_keys('a').send_keys(Keys.BACKSPACE).key_up(Keys.COMMAND)
        actions.send_keys('I have edited my CV')
        actions.perform()
        inputbox.submit()
        time.sleep(1)

        self.assertIn('I have edited my CV', self.browser.find_element_by_class_name('cv_text').text)

if __name__ == '__main__':  
    unittest.main(warnings='ignore')  