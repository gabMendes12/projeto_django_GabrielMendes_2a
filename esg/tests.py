from django.test import TestCase


class HomePageTests(TestCase):
    def test_impacta_page_is_available(self):
        response = self.client.get('/impacta/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Impacta ESG')

    def test_root_redirects_to_forum(self):
        response = self.client.get('/')

        self.assertRedirects(response, '/forum/')
