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

class Quote(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.IntegerField()
    message = models.TextField()

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