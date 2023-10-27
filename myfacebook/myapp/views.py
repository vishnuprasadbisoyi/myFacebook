from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from myapp.models import UserPost

# Create your views here.
def index(request):
    if request.method == "POST":
        uname = request.POST['username']
        pwd   = request.POST['password']
        user = authenticate(username=uname,password=pwd)
        if user is not None:
            login(request,user)
            return redirect('home')
    return render(request,'index.html')

@login_required(login_url='index')   
def home(request):
    userposts = UserPost.objects.filter(user=request.user)
    return render(request,'home.html',{'userposts':userposts})
   
@login_required(login_url='index')
def profile(request):

    if request.method=="POST":
        status = request.POST['status']
        loc    = request.POST['location']
        
        if len(status)>0:
            request.user.userprofile.status = status
        if len(loc)>0:
            
            request.user.userprofile.loc  = loc
        
        request.user.userprofile.save()
    return render(request,'profile.html')

def signout(request):
    logout(request)
    return redirect('index')

def signup(request):

    if request.method=='POST':

        uname = request.POST['username']
        pwd   = request.POST['password']
        user = User.objects.create(username=uname)
        user.set_password(pwd)
        user.save()
    return redirect("index")

@login_required(login_url='index')
def addPost(request):

    if request.method=='POST':

        post = request.POST['content']

        userpost = UserPost.objects.create(user=request.user, post=post)

        userpost.save()
    return redirect('home')