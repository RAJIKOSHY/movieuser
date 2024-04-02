from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        if not all([username, password, email, first_name, last_name]):
            return render(request, 'register.html', {'error': 'All fields are required.'})

        user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
        user.save()


        messages.success(request, 'Registration successful!')


        return redirect('/')
    else:
        return render(request, 'register.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request , user)
            return redirect('/')
        else:
            messages.info(request,"invalid")
            return redirect('login')
    return render(request,"login.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
