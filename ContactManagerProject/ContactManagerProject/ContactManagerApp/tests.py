"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

import django
from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse
from .models import Contact


class ContactManagerAppTest(TestCase):
    def setUp(self):
        Contact.objects.create(FirstName="lion", LastName="roar",Email="test@enzigma.com",MobileNo=89898989898)
        Contact.objects.create(FirstName="cat", LastName="meow",Email="test@enzigma.com",MobileNo=89898989898)

    def test_indexPage(self):        
        response = self.client.get(reverse('ContactManagerApp:contactList'))
        self.assertEqual(response.status_code, 200)

    def test_modify_contact_view(self):        
        response = self.client.get(reverse('ContactManagerApp:modify_contact',args=['1']))
        self.assertEqual(response.status_code, 200)

    def test_insert_contact_view(self):        
        response = self.client.get(reverse('ContactManagerApp:insert_contact'))
        self.assertEqual(response.status_code, 200)



   