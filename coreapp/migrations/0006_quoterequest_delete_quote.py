# Generated by Django 5.1.3 on 2024-12-18 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0005_alter_blogpost_date_posted'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuoteRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('project_type', models.CharField(choices=[('residential', 'Residential'), ('commercial', 'Commercial')], max_length=20)),
                ('project_size', models.CharField(max_length=100)),
                ('project_location', models.CharField(max_length=200)),
                ('preferred_contact_method', models.CharField(choices=[('email', 'Email'), ('phone', 'Phone'), ('both', 'Both')], max_length=20)),
                ('specific_project_details', models.TextField(blank=True, null=True)),
                ('preferred_materials', models.TextField(blank=True, null=True)),
                ('budget_constraints', models.CharField(blank=True, max_length=100, null=True)),
                ('timeline_preferences', models.CharField(blank=True, max_length=100, null=True)),
                ('date_submitted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Quote',
        ),
    ]
