from django.shortcuts import resolve_url as r
from django.test import TestCase

# from core.models import Item


class TestIndex(TestCase):
    def setUp(self):
        self.response = self.client.get(r('index'))

    def test_status_200(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'index.html')
    
    # def test_form(self):
    #     tags = (
    #         ('<form', 1),
    #         ('<input', 3),
    #         ('type="text"', 2),
    #         ('type="submit"', 1),
    #         ('name="csrfmiddlewaretoken"', 1),
    #         ('name="tab"', 1),
    #         ('name="value"', 1),

    #     )
        # for text, count in tags:
        #     with self.subTest():
        #         self.assertContains(self.response, text, count)
