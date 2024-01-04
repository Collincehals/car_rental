# Generated by Django 5.0 on 2024-01-04 19:02

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='brand_images')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='cars')),
                ('hire_rate_hour', models.DecimalField(decimal_places=2, max_digits=12)),
                ('hire_rate_day', models.DecimalField(decimal_places=2, max_digits=12)),
                ('lease_rate', models.DecimalField(decimal_places=2, max_digits=12)),
                ('mileage', models.DecimalField(decimal_places=2, max_digits=12)),
                ('transmission', models.CharField(blank=True, choices=[('manual', 'manual'), ('automatic', 'automatic')], max_length=400, null=True)),
                ('seats', models.IntegerField(blank=True, null=True)),
                ('luggage', models.IntegerField(blank=True, null=True)),
                ('fuel', models.CharField(blank=True, choices=[('petrol', 'petrol'), ('diesel', 'diesel'), ('electric', 'electric')], max_length=400, null=True)),
                ('description', models.CharField(blank=True, max_length=400, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
                ('id', models.CharField(default=uuid.uuid4, max_length=200, primary_key=True, serialize=False, unique=True)),
                ('brand', models.ManyToManyField(related_name='brands', to='a_main.brand')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('date_bookmarked', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
                ('id', models.CharField(default=uuid.uuid4, max_length=100, primary_key=True, serialize=False, unique=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('bookmark', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='a_main.car')),
            ],
            options={
                'ordering': ['-date_bookmarked'],
            },
        ),
        migrations.CreateModel(
            name='CarRental',
            fields=[
                ('rental_start_date', models.DateField()),
                ('rental_end_date', models.DateField()),
                ('pick_up_time', models.TimeField(max_length=200, null=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected'), ('completed', 'Completed')], default='pending', max_length=20)),
                ('pick_up_location', models.CharField(choices=[('Nairobi', 'Nairobi'), ('Nakuru', 'Nakuru'), ('Kiambu', 'Kiambu'), ('Mombasa', 'Mombasa'), ('Kisumu', 'Kisumu')], max_length=200, null=True)),
                ('drop_off_location', models.CharField(choices=[('Nairobi', 'Nairobi'), ('Nakuru', 'Nakuru'), ('Kiambu', 'Kiambu'), ('Mombasa', 'Mombasa'), ('Kisumu', 'Kisumu')], max_length=200, null=True)),
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
        migrations.CreateModel(
            name='TripBooking',
            fields=[
                ('pick_up_location', models.CharField(choices=[('Nairobi', 'Nairobi'), ('Nakuru', 'Nakuru'), ('Kiambu', 'Kiambu'), ('Mombasa', 'Mombasa'), ('Kisumu', 'Kisumu'), ('Kericho', 'Kericho'), ('Bungoma', 'Bungoma')], max_length=200, null=True)),
                ('drop_off_location', models.CharField(choices=[('Nairobi', 'Nairobi'), ('Nakuru', 'Nakuru'), ('Kiambu', 'Kiambu'), ('Mombasa', 'Mombasa'), ('Kisumu', 'Kisumu'), ('Kericho', 'Kericho'), ('Bungoma', 'Bungoma')], max_length=200, null=True)),
                ('pick_up_date', models.DateField(max_length=200)),
                ('drop_off_date', models.DateField(max_length=200)),
                ('pick_up_time', models.TimeField(max_length=200)),
                ('booking_number', models.CharField(default=uuid.uuid4, max_length=200, primary_key=True, serialize=False, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
    ]
