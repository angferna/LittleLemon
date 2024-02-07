from django import views
from django.contrib import admin 
from django.urls import include, path 
from . import views
from rest_framework.routers import DefaultRouter
from restaurant import views
# from .views import sayHello 
  
router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [ 
    # path('', sayHello, name='sayHello'), 
    path('', views.index, name='index'),
    #add following lines to urlpatterns list 
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('restaurant/booking/', include(router.urls))
]