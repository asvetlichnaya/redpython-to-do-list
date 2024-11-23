from django import forms
from .models import List, Item


class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['name']
        labels = {
            'name': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'List name'}),
        }


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'list', 'title', 'category', 'priority',
            'date', 'duration', 'completed', 'comments'
        ]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Item name'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'priority': forms.Select(attrs={'class': 'form-select'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control'}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'comments': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Any comments'}),
        }