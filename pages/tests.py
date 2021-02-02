# pages/tests.py
from django.test import SimpleTestCase
from django.urls import reverse

class HomepageTests(SimpleTestCase):
    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


    def test_homepage_url_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_homepage_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_homepage_contains_correct_html(self):
        response = self.client.get('/')
        self.assertContains(response, 'Homepage')


class AboutpageTests(SimpleTestCase):
    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)

    def test_aboutpage_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)


    def test_aboutpage_url_name(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_aboutpage_template(self):
        response = self.client.get('/about/')
        self.assertTemplateUsed(response, 'about.html')

    def test_aboutpage_contains_correct_html(self):
        response = self.client.get('/about/')
        self.assertContains(response, 'Aboutpage')


class ContactpageTests(SimpleTestCase):
    def setUp(self):
        url = reverse('contact')
        self.response = self.client.get(url)

    def test_contactpage_status_code(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)


    def test_contactpage_url_name(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)

    def test_contactpage_template(self):
        response = self.client.get('/contact/')
        self.assertTemplateUsed(response, 'contact.html')

    def test_contactpage_contains_correct_html(self):
        response = self.client.get('/contact/')
        self.assertContains(response, 'Contactpage')
