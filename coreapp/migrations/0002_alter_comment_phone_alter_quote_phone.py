# Generated by Django 5.1.3 on 2024-12-05 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='phone',
            field=models.IntegerField(max_length=20),
        ),
        migrations.AlterField(
            model_name='quote',
            name='phone',
            field=models.IntegerField(max_length=20),
        ),
    ]
