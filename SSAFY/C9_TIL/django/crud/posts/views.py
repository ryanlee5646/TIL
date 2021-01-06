from django.shortcuts import render, redirect
from .models import Post
# Create your views here.
# views.py -> urls.py -> templates
def new(request):
    return render(request, 'new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    
    # DB INSERT
    post = Post(title=title, content=content)
    post.save()
    
    return redirect(f'/posts/{post.pk}/')
    
def index(request):
    # All post
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts':posts})

def detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'detail.html', {'post': post})
    

# def naver(request, q):
#     return redirect(f'https://search.naver.com/search.naver?query={q}')
    
# def github(request, username):
#     return redirect(f'https://github.com/{username}')
    
def delete(request, post_id):
    post = Post.objects.get(pk=post_id)
    post.delete()
    return redirect('/posts/')
    
def edit(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'edit.html', {'post':post})
    
def update(request, post_id):
    post = Post.objects.get(pk=post_id)
    post.title = request.POST.get('title')
    post.content = request.POST.get('content')
    post.save()
    
    return redirect(f'/posts/{post_id}/')