from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect('posts:list')
        
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('posts:list')
    else:
        form = UserCreationForm()
    
    
    return render(request, 'signup.html', {'form':form} )
    
def login(request):
    if request.user.is_authenticated:
        return redirect('posts:list')
    
        
    # Session
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'posts:list')
    else:
        form = AuthenticationForm()
        
    request.GET.get('next') #=> /posts/new/    
    return render(request, 'login.html', {'form':form})
    
def logout(request):
    auth_logout(request)
    
    return redirect('posts:list')