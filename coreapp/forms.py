from django import forms
from coreapp.models import Contact, Quote, Comment, BlogPost


class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = '__all__'

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = '__all__'