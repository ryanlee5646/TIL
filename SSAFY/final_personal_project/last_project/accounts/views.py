from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model, update_session_auth_hash
from .forms import CustomUserChangeForm, ProfileForm, CustomUserCreationsForm
from .models import Profile
# Create your views here.

def signup(request): # 회원가입
    if request.user.is_authenticated:
        return redirect('movies:list')
    
    if request.method=='POST':
        signup_form = CustomUserCreationsForm(request.POST)
        if signup_form.is_valid():
            user=signup_form.save()
            Profile.objects.create(user=user)
            auth_login(request, user)
            return redirect('accounts:profile_update')
    else:
        signup_form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'signup_form':signup_form})
    
def login(request): # 로그인
    if request.user.is_authenticated:
        return redirect('posts:list')
    if request.method=='POST':
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            auth_login(request, login_form.get_user())
            return redirect(request.GET.get('next') or 'movies:list')
    else:
        login_form = AuthenticationForm()
    return render(request, 'accounts/login.html',{'login_form':login_form})

@login_required
def logout(request): # 로그아웃
    auth_logout(request)
    return redirect('movies:list')
    
#회원탈퇴
@login_required
def delete(request): 
    if request.method=='POST':
        request.user.delete()
        return redirect('movies:list')
    return render(request, 'accounts/delete.html')

@login_required
def password(request):
    if request.method=='POST':
        password_change_form = PasswordChangeForm(request.user, request.POST)
        if password_change_form.is_valid():
            user=password_change_form.save()
            return redirect('movies:list')
    else:
        password_change_form = PasswordChangeForm(request.user)
    return render(request, 'accounts/password.html',{'password_change_form':password_change_form})
        

def profile_update(request):
    profile=request.user.profile
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('accounts:check')
    else:
        profile_form = ProfileForm(instance=profile)
    return render(request,'accounts/profile_update.html', {'profile_form':profile_form})

def check(request):
    return render(request, 'accounts/check.html')