from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout

def main(request):
	return render(request,'index.html')

def user_login(request):
	tmp = ''
	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request,username = username, password=password)
		if user is not None:
			login(request,user=user)
			return redirect('/')
		tmp = 'Такого пользователя нет'
	return render(request,'login.html',{'pipi':tmp})

def user_logout(request):
	logout(request)
	return redirect('/')
