from django.shortcuts import render, redirect, get_object_or_404
from .models import List, Item
from django.forms import modelform_factory
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import ListForm, ItemForm


def index(request):
    return render(request, "lists/home_page.html")


@login_required(login_url='log_in')
def show_list(request):
    form = ListForm(request.POST)

    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            new_list = form.save(commit=False)
            new_list.user = request.user
            form.save()
            return redirect('show_list')
    else:
        form = ListForm()

    lists = List.objects.filter(user=request.user)
    items = Item.objects.filter(list__in = lists)
    category_names = [category[1] for category in Item.CATEGORY]

    return render(request, "lists/dashboard.html",
                  {"form": form, 'lists': lists, 'items': items, 'categories': category_names})


@login_required(login_url='log_in')
def remove_list(request, list_id):
    list = get_object_or_404(List, pk=list_id)

    list.delete()
    return redirect('show_list')


@login_required(login_url='log_in')
def remove_completed_items(request):
    items = Item.objects.all()

    for item in items:
        if item.completed:
            item.delete()
    return redirect('show_list')


@login_required(login_url='log_in')
def filter_items(request, category):

    lists = List.objects.filter(user=request.user)
    items = Item.objects.filter(list__in=lists)
    fields = [field.name for field in Item._meta.get_fields() if field.name != 'id']

    return render(request, "lists/filter_items.html", {'lists': lists, 'items': items, "category": category, "fields": fields})


@login_required(login_url='log_in')
def add_item(request, list_id):

    list = get_object_or_404(List, pk=list_id)
    form = ItemForm(request.POST)

    if request.method == 'POST':
        # form has been submitted, process data
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_list')
    else:
        form = ItemForm(initial={'list': list})
        form.fields['list'].queryset = List.objects.filter(user=request.user)

    return render(request, "lists/add_item.html", {"form": form, "list": list})


@login_required(login_url='log_in')
def edit_item(request, item_id):
    item = Item.objects.get(pk=item_id)

    ItemForm = modelform_factory(Item, fields=('list', 'title', 'category', 'priority', 'date', 'duration', 'completed', 'comments',))

    if request.method == 'POST':
        if 'save' in request.POST:
            form = ItemForm(request.POST, instance=item)
            if form.is_valid():
                form.save()
                return redirect('show_list')
        elif 'remove' in request.POST:
            item.delete()
            return redirect('show_list')
    else:
        form = ItemForm(instance=item)
        form.fields['list'].queryset = List.objects.filter(user=request.user)

    return render(request, "lists/edit_item.html", {"form": form})