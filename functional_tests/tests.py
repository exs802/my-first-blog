from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth.models import User
from django.test.client import Client
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from blog.models import CVItem
import time

class NewVisitorTest(StaticLiveServerTestCase):

    def setUp(self):
        CVItem.objects.create(title='Personal Info', text='email: exs802@student.bham.ac.uk')
        CVItem.objects.create(title='Work Experience', text='JLP, Apple, Ocado')
        CVItem.objects.create(title='Qualifications', text='GCSE')
        CVItem.objects.create(title='Education', text="Townley Grammar")
        self.browser = webdriver.Firefox()

        self.user = User.objects.create_superuser('testuser', 'exs802@student.bham.ac.uk', '12345')
        self.assertEqual(User.objects.all().count(), 1)
        
    def tearDown(self):
        self.browser.quit()

    def test_can_edit_and_save_cv(self):
        

        self.browser.get(self.live_server_url + '/admin/')
        username_input = self.browser.find_element_by_name("username")
        username_input.send_keys('testuser')
        password_input = self.browser.find_element_by_name("password")
        password_input.send_keys('12345')
        self.browser.find_element_by_xpath('//input[@value="Log in"]').click()

        self.browser.get(self.live_server_url)

        time.sleep(1)

        self.assertIn('Django Girls Blog', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text  
        self.assertIn('DJANGO GIRLS BLOG', header_text)

        self.browser.get(self.live_server_url + '/mycv')
        self.assertIn('ENIOLUWA SEGUN', self.browser.find_element_by_class_name('cv_name').text)

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

class NewSectionTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

        
        self.user = User.objects.create_superuser('testuser', 'exs802@student.bham.ac.uk', '12345')
        self.assertEqual(User.objects.all().count(), 1)
        
   
    def tearDown(self):
        self.browser.quit()

    def test_can_add_new_cv_section(self):
        self.browser.get(self.live_server_url + '/admin/')
        username_input = self.browser.find_element_by_name("username")
        username_input.send_keys('testuser')
        password_input = self.browser.find_element_by_name("password")
        password_input.send_keys('12345')
        self.browser.find_element_by_xpath('//input[@value="Log in"]').click()

        self.browser.get(self.live_server_url + '/mycv')
        self.assertIn('ENIOLUWA SEGUN', self.browser.find_element_by_class_name('cv_name').text)

        addSection = self.browser.find_element_by_id('id_add_section')

        addSection.click()
        time.sleep(1)

        inputbox = self.browser.find_element_by_class_name('cv-form')
        titlebox = self.browser.find_element_by_name('title')
        textbox = self.browser.find_element_by_name('text')

       
        actions = ActionChains(self.browser)
        actions.click(titlebox)
        actions.send_keys('New Section')
        actions.click(textbox)
        actions.send_keys('I have added a new section to my CV')
        actions.perform()
        inputbox.submit()
        time.sleep(2)

        textsections = self.browser.find_elements_by_class_name('cv_text')

        self.assertIn('I have added a new section to my CV', [textsection.text for textsection in textsections])

if __name__ == '__main__':  
    unittest.main(warnings='ignore')  