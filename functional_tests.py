from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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

        inputbox = self.browser.find_element_by_class_name('post-form')
        inputbox.send_keys('I have edited my CV')

        savebtn = self.browser.find_element_by_id('save btn btn-default')
        savebtn.click()
        time.sleep(1)

        self.assertIn('I have edited my CV', self.browser.find_element_by_class_name('cv_text'))

if __name__ == '__main__':  
    unittest.main(warnings='ignore')  