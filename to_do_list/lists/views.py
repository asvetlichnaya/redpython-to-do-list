from django.shortcuts import render
from lists.models import List, Item
# Create your views here.


def show_list(request):
    return render(request, "lists/home_page.html", {"lists": List.objects.all(), "items": Item.objects.all()})
