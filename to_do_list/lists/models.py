from django.db import models

# Create your models here.


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
    list = models.ForeignKey(List, related_name='items', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE)
    date = models.DateField()
    duration = models.IntegerField(default=1)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    comments = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.title}"

