from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerializer
from django.shortcuts import render

class MenuItemListView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

def home(request):
    # Logic for your home page view goes here
    return render(request, 'index.html', context={})  # Render the index.html template
