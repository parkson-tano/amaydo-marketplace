# Generated by Django 4.1 on 2022-08-14 12:28

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_rename_seller_product_owner_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='delivery_fee',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='free_delivery',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='name'),
        ),
    ]
