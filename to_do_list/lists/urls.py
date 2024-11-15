"""Defines URL patterns for lists."""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard', views.show_list, name='show_list'),
    path('remove-list/<int:list_id>', views.remove_list, name='remove_list'),
    path('add-item/<int:list_id>', views.add_item, name='add_item'),
    path('edit-item/<int:item_id>', views.edit_item, name='edit_item'),
    path('remove_completed_items', views.remove_completed_items, name='remove_completed_items'),
    path('category/<str:category>', views.filter_items, name='filter_items'),
]