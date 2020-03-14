from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm,SellForm
from django.contrib.auth.decorators import login_required
from blog.models import Post
from .forms import UserUpdateForm,ProfileUpdateForm 
def home(request):
	return render(request,'blog/home.html')
def prohome(request):
	return render(request,'blog/home.html')
def about(request):
	return render(request,'blog/about.html')
def contact(request):
	return render(request,'blog/contact.html')
def  register(request):
	if request.method== 'POST':
		form=UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username=form.cleaned_data.get('username')
			messages.success(request,f'Your account is created ,You can login')
			return redirect('login')
	else:
		form=UserRegisterForm()

	return render(request,'blog/register.html',{'form':form})
@login_required
def getmyitems(request):
	context={
		'items' : Post.objects.filter(author=request.user.username)
	}
	return render(request,'blog/myitems.html',context)
@login_required
def shop(request):
	context={
		'items' : Post.objects.all()
	}
	return render(request,'blog/shop.html',context)
@login_required
def profile(request):
	if request.method== 'POST':
		u_form=UserUpdateForm(request.POST,instance=request.user)
		p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request,f'Your account is updated ')
			return redirect('profile')
	else:
		u_form=UserUpdateForm(instance=request.user)
		p_form=ProfileUpdateForm(instance=request.user.profile)
	context={
		'u_form' :u_form,
		'p_form' :p_form
		
	}
	return render(request,'blog/profile.html',context)

@login_required
def get_name(request):
	
	if request.method == 'POST':
		
		form = SellForm(request.POST,request.FILES,author=request.user.username)
        
		if form.is_valid():
			print("in get_name")

			form.save()
			return redirect('blog-home')

	else :

		form=SellForm(author=request.user.username)

	
	return render(request, 'blog/sell.html', {'form': form})