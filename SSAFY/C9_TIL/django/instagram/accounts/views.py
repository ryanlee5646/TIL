from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import CustomUserChangeForm, ProfileForm, CustomUserCreationForm
from .models import Profile
# Create your views here.
def signup(request): #회원가입
    if request.user.is_authenticated: # 만약 로그인이 되있다면 리스트 페이지로 리다이렉트
        return redirect('posts:list')

    if request.method == 'POST':
        signup_form = CustomUserCreationForm(request.POST) #원래는 UserCreationForm()이나 forms.py에서 새로 forms를 적용해준걸 갖다씀
        if signup_form.is_valid():
            user = signup_form.save()   
            Profile.objects.create(user=user) # User의 Profile생성 (models.py에서 Profile import)
            
            auth_login(request, user) # 회원가입을 하면 로그인 된 상태로
            return redirect('posts:list')
    else:
        signup_form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'signup_form':signup_form})

def login(request): #로그인
    if request.user.is_authenticated:
        return redirect('posts:list')
    
    if request.method == 'POST':
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            auth_login(request, login_form.get_user())
            return redirect(request.GET.get('next') or 'posts:list') #원래 request.GET.get("next")가 없을때는 create창에서 로그인을해도 list로 갔으나
                                                                    # 앞에 함수를 추가해줌으로써 로그인했을때 create 창으로 넘겨줌
    
    else:
        login_form = AuthenticationForm() #import해줌
    return render(request, 'accounts/login.html', {'login_form': login_form})
    
def logout(request):
    auth_logout(request)
    return redirect('posts:list')
    
def people(request, username): #이 함수에 대한 url은 프로젝트 폴더 안에 있는 큰 url에 있음
    # get_user_model() => User
    people = get_object_or_404(get_user_model(), username=username) #상단에 import해주기(get_object_or_404 / get_user_model) 모두다
                                                #앞에 username 컬럼에 있는 username/ 뒤에 username은 주소값을 받아 넘겨온 username
    return render(request, 'accounts/people.html', {'people': people})
    
    
# 회원정보 수정(User Edit) - User CRUD 중 U
# from .forms import CustomUserChangeForm
@login_required  
def update(request):
    if request.method == 'POST':
        user_change_form = CustomUserChangeForm(request.POST, instance=request.user) # 요청된 정보와 로그인된 정보를 담아줌
        if user_change_form.is_valid():
            user_change_form.save()
            return redirect('people', request.user.username)
    else:
        user_change_form = CustomUserChangeForm(instance=request.user) # 어떤 user를 수정할 것인지 정보를 줘야함
    # CustomUserChangeForm을 하지 않으면 불필요한 정보들이 다 나옴
    return render(request, 'accounts/update.html', {'user_change_form': user_change_form, })

# User Delete(회원 탈퇴) - User CRUD 중 D
@login_required    
def delete(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('posts:list')
    return render(request, 'accounts/delete.html')

# from django.contrib.auth.forms import PasswordChangeForm  
# from django.contrib.auth import get_user_model, update_session_auth_hash
@login_required
def password(request):
    if request.method == 'POST':
        password_change_form = PasswordChangeForm(request.user, request.POST)
        if password_change_form.is_valid():
            user = password_change_form.save() # 변경된 비밀번호가 저장된 시점에서 이전에 계정이 만료됨
            update_session_auth_hash(request, user) # 변경된 유저의 정보를 만료된 자리에 바로 채워줌
            return redirect('people', request.user.username)
    else:
        password_change_form = PasswordChangeForm(request.user)
    return render(request, 'accounts/password.html', {'password_change_form': password_change_form})
    
    
def profile_update(request): #프로필 수정
    profile = request.user.profile
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile) # request.POST 는 nickname과 글, request.FILES는 사진, 이 것을 instacne=profile에 넣어서 수정
        if profile_form.is_valid():
            profile_form.save()
            return redirect('people', request.user.username)
    else:
        profile_form = ProfileForm(instance=profile) #forms.py 에있는 ProfileForm import
    return render(request, 'accounts/profile_update.html', {'profile_form': profile_form,})
    
def follow(request, user_id):
    people = get_object_or_404(get_user_model(), id=user_id) # 내가 follow하고하자는 사람
    
    # 만약 로그인된 유저가 이 people을 follow한 사람들 중에 있다면
    if request.user in people.followers.all():
    # 2. people을 unfollow 하기
        people.followers.remove(request.user)
    # 1. people를 follow 하기
    else:
        people.followers.add(request.user) # people를 follow하고자하는 followers에 현재 로그인유저(request.user)을 추가한다.
    return redirect('people', people.username)