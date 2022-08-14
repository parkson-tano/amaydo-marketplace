# Generated by Django 4.1 on 2022-08-14 08:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Verification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_type', models.CharField(choices=[('passport', 'Passport'), ('national ID', 'National ID Card'), ('others', 'Others')], default='national ID', max_length=50)),
                ('number', models.CharField(max_length=50)),
                ('photo_back', models.ImageField(upload_to='verification')),
                ('photo_front', models.ImageField(upload_to='verification')),
                ('is_verified', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('complete', 'complete'), ('in progress', 'in progress'), ('canceled', 'canceled')], max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(blank=True, max_length=300, null=True)),
                ('quater', models.CharField(blank=True, max_length=200, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('region', models.CharField(blank=True, max_length=256, null=True)),
                ('town', models.CharField(blank=True, max_length=256, null=True)),
                ('store_address', models.CharField(blank=True, max_length=256, null=True)),
                ('phone_number', models.IntegerField(blank=True, null=True)),
                ('image', models.ImageField(default='default.png', upload_to='profile_img')),
                ('verified', models.BooleanField(default=False)),
                ('account_type', models.CharField(choices=[('buyer', 'Buyer'), ('seller', 'Seller')], default='buyer', max_length=256)),
                ('date_of_birth', models.DateField(default=django.utils.timezone.now)),
                ('sponsored', models.BooleanField(default=False)),
                ('view_count', models.PositiveIntegerField(default=0)),
                ('joined_on', models.DateTimeField(auto_now_add=True)),
                ('favourite', models.ManyToManyField(blank=True, related_name='saved_user', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]