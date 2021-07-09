from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.utils import timezone
from .models import *
def signup(request):
    if request.method=="POST":
        # user has info and want account now.
        if request.POST['password1']==request.POST['password2']:
            # check if user name already exist.
            try:
                user=User.objects.get(username=request.POST['Username'])
                return render(request,'signup.html',{'error':'Username already taken'})
            except User.DoesNotExist:
                user=User.objects.create_user(request.POST['Username'],password=request.POST['password1'])
                auth.login(request,user) #this line log that user in.
                profile=UserDetail()
                profile.firstname=request.POST['firstname']
                profile.lastname=request.POST['lastname']
                profile.email=request.POST['email']
                profile.user=request.user
                profile.save()
                return redirect('createpost')
        else:
            return render(request,'signup.html',{'error':'please confirm password again'})
    else:
        # user wants to enter info.
        return render(request,'signup.html')



def login(request):
    if request.method=="POST":
        user = auth.authenticate(username=request.POST['Username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('createpost')
        else:
            return render(request,'login.html',{'error':'username or password is incorrect.'})
    else:
        return render(request,'login.html')



def logout(request):
    if request.method=="POST":
        auth.logout(request)
        return render(request,'signup.html')


def createpost(request):
    if request.method=='POST':
        detail=PostDetail()
        detail.user=request.user
        detail.text=request.POST['text']
        detail.created_at=timezone.datetime.now()
        detail.save()
        userdetail=PostDetail.objects.all()
        return render(request, 'userpost.html', {'userdetail':userdetail})

    else:
        return render(request, 'userpost.html')
