"""
URL configuration for to_do_list project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from lists.views import add_list, add_item, edit_item


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', add_list, name='add_list'),
    path('/add-item/<int:list_id>', add_item, name='add_item'),
    path('/<int:item_id>/edit-item/', edit_item, name='edit_item'),
]
