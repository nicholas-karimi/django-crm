from django.test import TestCase
from django.shortcuts import reverse
class IndexPageTest(TestCase):
    # Test status code
    def test_status_code(self):
        response = self.client.get(reverse('index'))
        # print(response.status_code)
        self.assertEqual(response.status_code, 200)

    def test_template_name(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, "landing.html")
