from django.contrib import admin
from coreapp.models import Member, Contact, Quote, Comment, BlogPost

# Register your models here.
admin.site.register(Member)
admin.site.register(Contact)
admin.site.register(Quote)
admin.site.register(Comment)
admin.site.register(BlogPost)
