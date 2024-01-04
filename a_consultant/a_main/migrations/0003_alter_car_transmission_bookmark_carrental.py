# Generated by Django 5.0 on 2024-01-04 10:14

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_main', '0002_rename_hire_rate_car_hire_rate_day_car_fuel_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='transmission',
            field=models.CharField(blank=True, choices=[('manual', 'manual'), ('automatic', 'automatic')], max_length=400, null=True),
        ),
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_bookmarked', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
                ('bookmark', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='a_main.car')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CarRental',
            fields=[
                ('rental_start_date', models.DateField()),
                ('rental_end_date', models.DateField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected'), ('completed', 'Completed')], default='pending', max_length=20)),
                ('pick_up_location', models.CharField(max_length=200)),
                ('drop_off_location', models.CharField(max_length=200)),
                ('pick_up_date', models.DateField(max_length=200)),
                ('drop_off_date', models.DateField(max_length=200)),
                ('pick_up_time', models.TimeField(max_length=200)),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
                ('renting_id', models.CharField(default=uuid.uuid4, max_length=200, primary_key=True, serialize=False, unique=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='a_main.car')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_ordered'],
            },
        ),
    ]