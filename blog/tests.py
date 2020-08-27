from django.test import TestCase
from blog.models import CVItem

# Create your tests here.
class CVPageTest(TestCase):
    def test_uses_home_page_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'blog/home_page.html')
    
    def test_uses_cv_page_template(self):
        response = self.client.get('/mycv/')
        self.assertTemplateUsed(response, 'blog/show_cv.html')

    def test_display_database_cv_sections(self):
        CVItem.objects.create(title='Qualifications', text='GCSE')
        CVItem.objects.create(title='Education', text="Townley Grammar")

        saved_items = CVItem.objects.all()

        response = self.client.get('/mycv/')

        self.assertEqual(saved_items.count(), 2)

        self.assertIn('Qualifications', response.content.decode())
        self.assertIn('Education', response.content.decode())
        self.assertIn('GCSE', response.content.decode())
        self.assertIn('Townley Grammar', response.content.decode())
    
    def test_uses_edit_cv_template(self):
        CVItem.objects.create(title='Qualifications', text='GCSE')
        response = self.client.get('/editcv/1/')
        self.assertTemplateUsed(response, 'blog/edit_cv.html')


class ItemModelTest(TestCase):

    def test_saving_and_retrieving_info(self):

        personal_info = CVItem()
        personal_info.title = 'Personal Information'
        personal_info.text = 'email: exs802@student.bham.ac.uk'
        personal_info.save()

        work_exp = CVItem()
        work_exp.title = 'Work Experience'
        work_exp.text = 'JLP, Apple, Ocado'
        work_exp.save()

        saved_items = CVItem.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'email: exs802@student.bham.ac.uk')
        self.assertEqual(second_saved_item.text, 'JLP, Apple, Ocado')
