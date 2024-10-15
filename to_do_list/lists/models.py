from django.db import models

# Create your models here.


class List(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"


class Item(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20)
    priority = models.CharField(max_length=20)
    date = models.DateField()
    duration = models.IntegerField(default=1)
    status = models.CharField(max_length=20)
    comments = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.title}"

