from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from . forms import sign_upForm
from . forms import UploadForm
from . models import Items
from django.core.files.storage import FileSystemStorage
from django.conf.urls import url


@login_required
def index(request):
    return render(request, 'accounts/index.html')

def home(request):
    return render(request, 'home.html')

def tutoring(request):
    return render(request, 'accounts/tutoring.html')

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return render(request, "registration/logged_out.html")

def sign_up(request):
    context = {}
    form = sign_upForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, 'accounts/index.html')
    context['form'] = form
    return render(request, 'registration/sign_up.html', context)

def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'accounts/upload.html', context)

def upload_item(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gratitude')
    else:
        form = UploadForm()
    return render(request, 'accounts/upload_item.html', {
        'form': form
    })

def upload_list(request):
    items = Items.objects.all()
    return render(request, 'accounts/upload_list.html',{
        'items': items
    })
def about(request):
    return render(request, 'about.html')
def gratitude(request):
    return render(request, 'accounts/gratitudepage.html')