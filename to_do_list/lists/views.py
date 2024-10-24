from django.shortcuts import render, redirect, get_object_or_404
from .models import List, Item
from django.forms import modelform_factory
from datetime import date


def add_list(request):
    ListForm = modelform_factory(List, fields=('name',))

    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_list')
    else:
        form = ListForm()

    lists = List.objects.all()
    items = Item.objects.all()

    return render(request, "lists/home_page.html", {"form": form, 'lists': lists, 'items': items})


def remove_list(request, list_id):
    ListForm = modelform_factory(List, fields=('name',))
    list = get_object_or_404(List, pk=list_id)

    list.delete()
    form = ListForm()
    lists = List.objects.all()
    items = Item.objects.all()

    return render(request, "lists/home_page.html", {"form": form, 'lists': lists, 'items': items})


def remove_completed_items(request):
    ListForm = modelform_factory(List, fields=('name',))
    items = Item.objects.all()

    for item in items:
        if item.completed:
            item.delete()

    form = ListForm()
    lists = List.objects.all()
    items = Item.objects.all()

    return render(request, "lists/home_page.html", {"form": form, 'lists': lists, 'items': items})

# not yet ready
def filter_items(request):
    ListForm = modelform_factory(List, fields=('name',))
    items = Item.objects.all()
    lists = List.objects.all()

    filtered_items = []
    for item in items:
        if item.date == date.today():
            filtered_items.append(item)

    form = ListForm()

    return render(request, "lists/home_page.html", {"form": form, 'lists': lists, 'items': filtered_items})


def add_item(request, list_id):
    list = get_object_or_404(List, pk=list_id)
    ItemForm = modelform_factory(Item, fields=('list', 'title', 'category', 'priority', 'date', 'duration', 'completed', 'comments',))

    if request.method == 'POST':
        # form has been submitted, process data
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_list')
    else:
        form = ItemForm(initial={'list': list})

    return render(request, "lists/add_item.html", {"form": form, "list": list})


def edit_item(request, item_id):
    item = Item.objects.get(pk=item_id)

    ItemForm = modelform_factory(Item, fields=('list', 'title', 'category', 'priority', 'date', 'duration', 'completed', 'comments',))

    if request.method == 'POST':
        if 'save' in request.POST:
            form = ItemForm(request.POST, instance=item)
            if form.is_valid():
                form.save()
                return redirect('add_list')
        elif 'remove' in request.POST:
            item.delete()
            return redirect('add_list')
    else:
        form = ItemForm(instance=item)

    return render(request, "lists/edit_item.html", {"form": form})
