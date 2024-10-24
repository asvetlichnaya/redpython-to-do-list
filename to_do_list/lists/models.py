from django.db import models
from datetime import date


class List(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"


class Priority(models.Model):
    name = models.CharField(max_length=20)
    value = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.name}"


class Status(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}"


class Item(models.Model):
    PRIORITY = {
        "1": "High",
        "2": "Meddium",
        "3": "Low"
    }
    list = models.ForeignKey(List, related_name='items', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20)
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY,
        default=3,
    )
    date = models.DateField(default=date.today)
    duration = models.IntegerField(default=1)
    completed = models.BooleanField(default=False)
    comments = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.title}"

