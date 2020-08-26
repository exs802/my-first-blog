from django.test import TestCase

# Create your tests here.
class CVPageTest(TestCase):
    def test_uses_home_page_template(self):
        response = response = self.client.get('/')
        self.assertTemplateUsed(response, 'blog/home_page.html')
