# pages/tests.py
from django.test import SimpleTestCase
from django.urls import reverse

class HomepageTests(SimpleTestCase):
    def test_homepage_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


    def test_homepage_url_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)


class AboutpageTests(SimpleTestCase):
    def test_aboutpage_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)


    def test_aboutpage_url_name(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)


class ContactpageTests(SimpleTestCase):
    def test_contactpage_status_code(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)


    def test_contactpage_url_name(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
