# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.
class SimpleTest(TestCase):
    
    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
