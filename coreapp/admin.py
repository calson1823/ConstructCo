from django.contrib import admin
from coreapp.models import Member, Contact, Comment, BlogPost, QuoteRequest

# Register your models here.
admin.site.register(Member)
admin.site.register(Contact)
admin.site.register(QuoteRequest)
admin.site.register(Comment)
admin.site.register(BlogPost)
