# Generated by Django 4.1 on 2022-08-14 08:07

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='products')),
                ('marked_price', models.PositiveIntegerField()),
                ('selling_price', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('quantity', models.IntegerField(default=0)),
                ('town', models.CharField(blank=True, max_length=256, null=True)),
                ('warranty', models.CharField(blank=True, max_length=300, null=True)),
                ('return_policy', models.CharField(blank=True, max_length=300, null=True)),
                ('contact', models.BigIntegerField(blank=True, null=True)),
                ('view_count', models.PositiveIntegerField(default=0)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from=('title', 'date_created'), unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category')),
                ('seller', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products.image/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered_by', models.CharField(max_length=200)),
                ('shipping_address', models.CharField(max_length=200)),
                ('mobile', models.CharField(max_length=10)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('subtotal', models.PositiveIntegerField()),
                ('discount', models.PositiveIntegerField()),
                ('total', models.PositiveIntegerField()),
                ('order_status', models.CharField(choices=[('Order Recieved', 'Order Recieved'), ('Order Processing', 'Order Processing'), ('On the way', 'On the way'), ('Order Complete', 'Order Complete'), ('Order Cancel', 'Order Cancel')], default='Order Recieved', max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('payment_method', models.CharField(choices=[('Cash On Delivery', 'Cash On Delivery'), ('Mobile Money', 'Mobile Money')], default='Cash On Delivery', max_length=20)),
                ('payment_completed', models.BooleanField(blank=True, default=False, null=True)),
                ('cart', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='product.cart')),
            ],
        ),
        migrations.CreateModel(
            name='CartProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.PositiveIntegerField(default=1)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('subtotal', models.PositiveIntegerField(default=1)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
    ]