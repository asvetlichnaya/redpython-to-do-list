# Generated by Django 5.1.2 on 2024-10-15 17:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0003_priority_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='priority',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lists.priority'),
        ),
        migrations.AlterField(
            model_name='item',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lists.status'),
        ),
    ]
