from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm,SellForm
from django.contrib.auth.decorators import login_required
from blog.models import Post
def home(request):
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
		'items' : Post.objects.filter(author=request.user)
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
	return render(request,'blog/profile.html')

@login_required
def get_name(request):
	
	if request.method == 'POST':
		
		form = SellForm(request.POST,user=request.user.username)
        
		if form.is_valid():
			print("in get_name")

			form.save()
			return redirect('blog-home')

	else :

		form=SellForm(user=request.user.username)

	
	return render(request, 'blog/sell.html', {'form': form})