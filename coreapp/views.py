from django.shortcuts import render, redirect

from coreapp.forms import QuoteForm, ContactForm, CommentForm, BlogPostForm
from coreapp.models import Member, Contact, Comment, Quote, BlogPost


# Create your views here.
def index(request):
    if request.method == 'POST':
        if Member.objects.filter(
                email=request.POST['email'],
                password=request.POST['password'],
        ).exists():
            members = Member.objects.get(
                email=request.POST['email'],
                password=request.POST['password'],
            )
            return render(request, 'index.html', {'members': members})
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    images = BlogPost.objects.all()
    return render(request, 'blog.html', {"images": images})

def blog_details(request):
    if request.method == 'POST':
        mycomment = Comment(
            name = request.POST.get('name'),
            email = request.POST.get('email'),
            phone = request.POST.get('phone'),
            comment = request.POST.get('comment'),
        )
        mycomment.save()
        return redirect('/showcomment')

    else:
        return render(request, 'blog-details.html')

def showcomment(request):
    allcomments = Comment.objects.all()
    return render(request, 'showcomment.html', {"comment": allcomments})

def contact(request):
    if request.method == 'POST':
        mycontact = Contact(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message'],
        )
        mycontact.save()
        return redirect('/showcontact')

    else:
        return render(request, 'contact.html')

def showcontact(request):
    allcontacts = Contact.objects.all()
    return render(request, 'showcontact.html', {"contact": allcontacts})

def project_details(request):
    return render(request, 'project-details.html')

def projects(request):
    return render(request, 'projects.html')

def service_details(request):
    return render(request, 'service-details.html')

def services(request):
    return render(request, 'services.html')

def starter_page(request):
    return render(request, 'index.html')

def register(request):
    if request.method == "POST":
        members = Member(
            name=request.POST['name'],
            email=request.POST['email'],
            password=request.POST['password']
        )
        members.save()
        return redirect('/login')
    else:
        return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def quote(request):
    if request.method == "POST":
        myquote=Quote(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            message=request.POST['message'],
        )
        myquote.save()
        return redirect('/quote')

    else:
        return render(request, 'quote.html')

def upload_blog(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            ''
            form.save()
            return redirect('/blog')
    else:
        form = BlogPostForm()
    return render(request, 'upload-blog.html', {'form': form})
