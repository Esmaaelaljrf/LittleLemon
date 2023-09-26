# from django.test import TestCase

# class MenuViewTest(TestCase):

# test_views.py

from django.test import TestCase
from restaurant.models import Menu
from django.urls import reverse
import json

class MenuViewTest(TestCase):
    def setUp(self):
        # Add test instances of the Menu model
        Menu.objects.create(name='Menu 1', price=10)
        Menu.objects.create(name='Menu 2', price=15)
        Menu.objects.create(name='Menu 3', price=20)

    def test_getall(self):
        # Retrieve all Menu objects
        response = self.client.get(reverse('menu-list'))
        menus = Menu.objects.all()

        # Serialize the retrieved objects
        serialized_data = json.dumps([{'name': menu.Title, 'price': menu.Price} for menu in menus])

        # Check if the serialized data equals the response
        self.assertEqual(response.content.decode(), serialized_data)