# Generated by Django 5.1.2 on 2024-10-14 22:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=20)),
                ('priority', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('duration', models.IntegerField(default=1)),
                ('status', models.CharField(max_length=20)),
                ('comments', models.CharField(max_length=200)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lists.list')),
            ],
        ),
    ]
