from django.test import TestCase

from core.models import Item


class ItemTestBase(TestCase):
    def setUp(self):
        ...