from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from Login_App.models import UserProfile, Follow
from Posts_App.models import Post,Like
from Posts_App.forms import PostForm

# Create your views here.
@login_required
def home(request):
    following_list = Follow.objects.filter(follower=request.user)
    posts = Post.objects.filter(author__in=following_list.values_list('following'))
    like_post = Like.objects.filter(user=request.user)
    liked_post_list = like_post.values_list('post', flat=True)
    if request.method == 'GET':
        search = request.GET.get('search','')
        result = User.objects.filter(username__icontains=search)
    return render(request,'Posts_App/home.html',context={'title':'Home','search':search,'result':result,
                                                         'posts':posts,'liked_post_list':liked_post_list}) 
    
def update_post(request,pk):
    post = Post.objects.get(pk=pk)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('Login_App:profile'))
             
    return render(request,'Posts_App/update_post.html',context={'form':form,'post':post})

def delete_post(request,pk):
    post = Post.objects.get(pk=pk).delete()
    return HttpResponseRedirect(reverse('Login_App:profile'))
    
    
       







@login_required
def like(request,pk):
    post = Post.objects.get(pk=pk)
    already_liked = Like.objects.filter(post=post,user=request.user)
    if not already_liked:
        like_post = Like(post=post,user=request.user)
        like_post.save()
    return HttpResponseRedirect(reverse('Posts_App:home'))
    

@login_required
def unlike(request,pk):
    post = Post.objects.get(pk=pk)
    already_liked = Like.objects.filter(post=post,user=request.user)
    already_liked.delete()

    return HttpResponseRedirect(reverse('Posts_App:home'))
  