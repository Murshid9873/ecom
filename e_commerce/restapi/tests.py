from django.test import TestCase
from django.urls import reverse, resolve
from rest_framework.test import APIClient
from rest_framework import status
# Create your tests here.

class TestSample(TestCase):

    def setup(self):
        self.client = APIClient

    def test_index(self):
        url = reverse('rest:index')
        res = self.client.get(url) # to get the response from the server

        self.assertEqual(res.data, 'congratulations, you have created an API')    

    
    def test_number(self):
        url = reverse('rest:float')
        res = self.client.get(url)

        data = res.data

        if type(data) != float:
            self.fail('not a floating point')

