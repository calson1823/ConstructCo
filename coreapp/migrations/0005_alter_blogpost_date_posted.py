# Generated by Django 5.1.3 on 2024-12-06 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0004_alter_blogpost_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='date_posted',
            field=models.DateField(),
        ),
    ]
