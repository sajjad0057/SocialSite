from django.shortcuts import render,HttpResponse, HttpResponseRedirect
from Login_App.forms import CreateNewUserForm,LoginForm,EditProfile
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from Login_App.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from Posts_App.forms import PostForm
from Login_App.models import Follow


  
# Create your views here.



def index(request):
    return HttpResponseRedirect(reverse('Login_App:sign_up'))

def sign_up(request):
    form = CreateNewUserForm()
    registered = False
    if request.method == 'POST':
        form = CreateNewUserForm(request.POST)
        if form.is_valid():
            created_user = form.save()
            registered = True
            user_profile = UserProfile(user=created_user)
            user_profile.save()     
        
    return render(request,'Login_App/sign_up.html',context={'title':'Sign Up SocialSite','form':form,
                                                    'registered':registered})
def login_page(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
              username=form.cleaned_data.get('username')
              password=form.cleaned_data.get('password')
              xxx = authenticate(username=username, password=password)
              if xxx is not None:
                  login(request,xxx)
                  return HttpResponseRedirect(reverse('Posts_App:home'))
    return render(request,'Login_App/login.html',context={'title':'login','form':form})

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('Login_App:login'))
    
    
     

@login_required
def edit_profile(request):
    form = EditProfile(instance=request.user.user_profile)
    if request.method == 'POST':
        form = EditProfile(request.POST,request.FILES,instance=request.user.user_profile)
        if form.is_valid():
            form.save()
            form = EditProfile(instance=request.user.user_profile)
            return HttpResponseRedirect(reverse('Login_App:profile'))
    return render(request,'Login_App/edit_profile.html',context={'form':form,'title':'Edit profile'})

@login_required  
def profile(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect(reverse('Login_App:profile'))
             
    return render(request,'Login_App/profile.html',context={'form':form})

@login_required
def user_profile(request,username):
    search_user = User.objects.get(username=username)
    already_follow = Follow.objects.filter(follower=request.user,following=search_user)
    if search_user == request.user:
        return HttpResponseRedirect(reverse('Login_App:profile'))
    return render(request,'Login_App/user_profile.html',context={'search_user':search_user,'already_follow':already_follow})

@login_required
def follow(request,username):
    following_user = User.objects.get(username=username)
    follower_user = request.user
    already_follow = Follow.objects.filter(follower=follower_user,following=following_user)
    if not already_follow:
        followed_user = Follow(follower=follower_user,following=following_user)
        followed_user.save()
    return HttpResponseRedirect(reverse('Login_App:user_profile',kwargs={'username':username}))

@login_required
def unfollow(request,username):
    following_user = User.objects.get(username=username)
    follower_user = request.user
    already_follow = Follow.objects.filter(follower=follower_user,following=following_user)
    if already_follow:
        already_follow.delete()
        return HttpResponseRedirect(reverse('Login_App:user_profile',kwargs={'username':username}))
    
    
        
        
    


               