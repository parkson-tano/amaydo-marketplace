# Generated by Django 4.1 on 2022-08-14 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_rename_image_userprofile_profilr_pic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='profilr_pic',
            new_name='profile_pic',
        ),
    ]
