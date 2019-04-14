from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.
def signup(request):
    if request.method=='post':
        if request.post['password1'] == request.post['password2']:
            try:
                user = User.objects.get(username=request.post['username'])
                return render(request, 'accounts/signup.html', {'error': 'Username is already taken'})
            except User.DoesNotExist:
                 user=User.objects.create_user(request.post['username'],password=request.post['password1'])
                 auth.login(request,user)
                 return redirect('home')
        else:
            return render(request, 'accounts/signup.html',{'error':'Password doesn\'t matched'})
    else:
        return render(request,'accounts/signup.html')


def login(request):
    return render(request,'accounts/login.html')




def logout(request):
    return render(request,'accounts/logout.html')