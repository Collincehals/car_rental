# Generated by Django 5.0 on 2024-02-04 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('a_main', '0002_carrental_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrental',
            name='name',
        ),
    ]
