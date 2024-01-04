# Generated by Django 5.0 on 2024-01-04 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_main', '0008_remove_carrental_drop_off_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrental',
            name='drop_off_location',
            field=models.CharField(choices=[('Nairobi', 'Nairobi'), ('Nakuru', 'Nakuru'), ('Kiambu', 'Kiambu'), ('Mombasa', 'Mombasa'), ('Kisumu', 'Kisumu')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='carrental',
            name='pick_up_location',
            field=models.CharField(choices=[('Nairobi', 'Nairobi'), ('Nakuru', 'Nakuru'), ('Kiambu', 'Kiambu'), ('Mombasa', 'Mombasa'), ('Kisumu', 'Kisumu')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='carrental',
            name='pick_up_time',
            field=models.TimeField(max_length=200, null=True),
        ),
    ]
