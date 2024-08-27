# Generated by Django 5.0.7 on 2024-07-13 07:34

import django.db.models.deletion
import users.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_location_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.location'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(null=True, upload_to=users.utils.user_directory_path),
        ),
    ]
