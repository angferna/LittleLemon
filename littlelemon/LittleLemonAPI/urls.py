from django.urls import path
from . import views

urlpatterns = [
    path('menu-items/', views.MenuItemListView.as_view(), name='menu_item_list'),
    path('menu-items/<int:pk>/', views.SingleMenuItemView.as_view(), name='single_menu_item'),
]
