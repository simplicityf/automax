# Generated by Django 5.0.7 on 2024-07-19 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='Image',
            new_name='image',
        ),
        migrations.AlterField(
            model_name='listing',
            name='color',
            field=models.CharField(max_length=24),
        ),
    ]
