from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User, auth 
from django.contrib.auth import logout as auth_logout
from django.contrib.sessions.models import Session
from django.contrib import messages
from .models import Profile, Post


# Create your views here.

@login_required(login_url='signin')
def index(request):

    return render(request, 'index.html')

@login_required(login_url='signin')
def upload(request):
    if request.method=='POST':
        user = request.user.username
        image = request.FILES.get('image_uplaod')
        caption = request.POST['caption']

        new_post = Post.objects.create(user=user, image=image, caption=caption)
        new_post.save()

        return redirect('/')
    else:
        return redirect('/')

@login_required(login_url='signin')
def settings(request):
    return render(request, 'setting.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email is already taken')
                return redirect('signup')
                
            else:
                user = User.objects.create_user(username=username, email=email, password=password2)
                user.save()

                #login user and redirect to settings
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)

                #create a profile for a new user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('settings')
        else:
            messages.info(request, 'Password Not Matching')
            return redirect('signup')
    else:
        return render(request, 'signup.html')

def signin(request):

    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('signin')
    else:
        return render(request, 'signin.html')

@login_required(login_url='signin')
def logout(request):
    auth_logout(request)
    request.session.flush()
    return redirect('signin')
