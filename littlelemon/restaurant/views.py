from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, viewsets, permissions
from rest_framework.decorators import api_view
from .models import MenuItem, Booking
from .serializers import MenuItemSerializer, UserSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated

# def sayHello(request):
#  return HttpResponse('Hello World')

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

# views.py in the restaurant app package folder

# Create your views here. 
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [permissions.IsAuthenticated] 