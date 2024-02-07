from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from models import Menu
from serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        # Add test instances of the Menu model
        Menu.objects.create(name='Pizza', description='Delicious pizza', price=10.99)
        Menu.objects.create(name='Burger', description='Tasty burger', price=8.99)

    def test_getall(self):
        # Retrieve all the Menu objects added for the test purpose
        client = APIClient()
        url = reverse('menu-list')  # Assuming 'menu-list' is the URL name for listing menus
        response = client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.data, serializer.data)
