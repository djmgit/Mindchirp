from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Post
from django.template import loader
from django.http import Http404
from django .core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.utils import timezone




def home(request):
    posts=Post.objects.order_by('-pub_date')
    users=User.objects.all
    context={'posts':posts,'user':request.user,'users':users}
    return render(request,'social_network/home.html',context)

def user_login(request):
    posts=Post.objects.order_by('-pub_date')
    return render(request,'social_network/login.html')

def user_signup(request):
    
    return render(request,'social_network/signup.html')    

def user_auth(request):
	uname=request.POST['username']
	passd=request.POST['password']

	user=authenticate(username=uname,password=passd)
	if user is not None:
		if user.is_active:
			login(request,user)
			return HttpResponseRedirect(reverse('social_network:home'))    

def signup_auth(request):
	uname=request.POST['username']
	passd=request.POST['password']
	email=request.POST['email']

	user=User.objects.create_user(uname,email,passd)
	user.first_name=request.POST['firstname']
	user.last_name=request.POST['lastname']

	user.save()

	return HttpResponseRedirect(reverse('social_network:user_login'))

			
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('social_network:user_login'))	

def add_status(request):
	status=request.POST['status']
	post=Post(post_text=status,pub_date=timezone.now(),username=request.user.username,image=request.FILES['image'])
	post.save()
	return HttpResponseRedirect(reverse('social_network:home'))

def add_comment(request,post_id):
	post=get_object_or_404(Post,pk=post_id)
	comment=request.POST['comment']
	c=post.comment_set.create(comment_text=comment,username=request.user.username)
	c.save()
	return HttpResponseRedirect(reverse('social_network:home'))

def user_wall(request):
	posts=Post.objects.filter(username=request.user.username).order_by('-pub_date')
	users=User.objects.all
	context={'posts':posts,'user':request.user,'users':users}
	return render(request,'social_network/user_info.html',context)

def show_user(request,user_id):
	user=get_object_or_404(User,pk=user_id)
	posts=Post.objects.filter(username=user.username).order_by('-pub_date')
	users=User.objects.all
	context={'posts':posts,'user':request.user,'users':users}
	return render(request,'social_network/view_user.html',context)	





