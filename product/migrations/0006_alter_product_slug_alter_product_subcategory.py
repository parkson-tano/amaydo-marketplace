# Generated by Django 4.1 on 2022-08-23 09:38

import autoslug.fields
from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_product_slug_subcategory_product_subcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from=('name',), unique_with=['owner__userprofile__id', 'date_created']),
        ),
        migrations.AlterField(
            model_name='product',
            name='subcategory',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, blank=True, chained_field='category', chained_model_field='category', null=True, on_delete=django.db.models.deletion.CASCADE, to='product.subcategory'),
        ),
    ]