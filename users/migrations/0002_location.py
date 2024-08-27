# Generated by Django 5.0.7 on 2024-07-11 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_1', models.CharField(blank=True, max_length=140)),
                ('address_2', models.CharField(blank=True, max_length=140)),
                ('city', models.CharField(max_length=140)),
            ],
        ),
    ]