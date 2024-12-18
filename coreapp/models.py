from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name

class QuoteRequest(models.Model):
    PROJECT_TYPES = [
        ('residential', 'Residential'),
        ('commercial', 'Commercial'),
    ]

    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    project_type = models.CharField(max_length=20, choices=PROJECT_TYPES)
    project_size = models.CharField(max_length=100)
    project_location = models.CharField(max_length=200)
    preferred_contact_method = models.CharField(max_length=20, choices=[('email', 'Email'), ('phone', 'Phone'), ('both', 'Both')])
    specific_project_details = models.TextField(blank=True, null=True)
    preferred_materials = models.TextField(blank=True, null=True)
    budget_constraints = models.CharField(max_length=100, blank=True, null=True)
    timeline_preferences = models.CharField(max_length=100, blank=True, null=True)
    date_submitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    image = models.ImageField(upload_to='images/')
    date_posted = models.DateField()
    title = models.CharField(max_length=100)
    subtitle1 = models.CharField(max_length=100)
    subtitle2 = models.CharField(max_length=100)
    body = models.TextField()
    footer = models.TextField()

    def __str__(self):
        return self.title