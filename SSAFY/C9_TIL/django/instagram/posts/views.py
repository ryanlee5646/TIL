from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from .forms import PostForm, CommentForm, ImageFormSet
from .models import Post, Comment
from django.db import transaction
from itertools import chain
from django.http import JsonResponse
# Create your views here.


def explore(request): # 내가 팔로우 안한 사람들 posts까지 다 보임
    posts= Post.objects.order_by('-id').all()
    comment_form = CommentForm() #리스트페이지에 포스트마다 댓글이 보이도록
    return render(request, 'posts/list.html', {'posts': posts, 'comment_form': comment_form})

@login_required #로그인해야 내가 follow한 사람들에 대한 post가 보이기 때문 
def list(request):
    # posts = Post.objects.order_by('-id').all() # order_by('')는 게시물을 오름차순으로 정렬 id값의 -를 붙여줌으로써 내림차순으로 정렬
    
    # 1. 내가 follow하고 있는 사람들의 리스트
    followings = request.user.followings.all() # 로그인한사람이 현재 팔로우하고 있는 리스트
    # 2. followings 변수와 나를 묶음
    followings = chain(followings, [request.user])
    # 2. 이 사람들이 작성한 Post들만 뽑아옴.
    posts = Post.objects.filter(user__in=followings).order_by('-id') # user__in(언더바를 2개쓰게되면 리스트 형태로 들어감)
    comment_form = CommentForm() #리스트페이지에 포스트마다 댓글이 보이도록
    return render(request, 'posts/list.html', {'posts': posts, 'comment_form': comment_form})


#decorator 함수 호출
@login_required # 로그인을 해야지만 함수가 실행되도록 함(decorator 역할)
def create(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST) #앞에 인자값에는 data=, files=가 생략 되있다 request.POST = Post방식으로 담겨져있는 데이터
        image_formset = ImageFormSet(request.POST, request.FILES)
        # request.FILES는 사진파일이 담겨져있는 데이터
        if post_form.is_valid() and image_formset.is_valid(): #post_form에 담긴 data가 database에 넣어줘도 되는지 여부 판단/ image_formset에 담긴 데이터도 유효한지 확인
            post = post_form.save(commit=False) #post에 받아온 데이터를 저장 
            post.user = request.user # post.user에 현재 로그인된 user정보 저장
            
        with transaction.atomic(): # 메서드를 import 해줘야함
        # 이 코드는 아래에 코드 순서대로 실행이 되도록 보장해주는 코드(매우중요)
        # 풀어서 말하면 post가 생선된 이후에 이미지를 만들도록 (순서가 뒤바뀌지 않게)
            # 첫번째
            post.save() # 실제 데이터베이스에 저장
            # 두번째
            image_formset.instance = post # image_formset가 어디에 속한 것인지. forms.py에서 ImageFormSet에서 부모(post)가 속한 정보가 된다.(첫번째 인스턴스)
            image_formset.save() # 실제 데이터베이스에 저장
            return redirect('posts:list')
    else:
        post_form = PostForm()
        image_formset = ImageFormSet() # (0415) forms.py에서 새로 만든 모델
    return render(request, 'posts/form.html', {'post_form': post_form, 'image_formset': image_formset}) 
    #이제 template관리를 위해 App이름을 명시해주기로 함.(앞으로 app이 여러개 생기므로) 

@login_required
def update(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    if post.user != request.user: # 다른 사람의 글을 함부로 수정하지 못하도록 막음
        return redirect('posts:list')
    
    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=post)
        image_formset = ImageFormSet(request.POST, request.FILES, instance=post)
        if post_form.is_valid() and image_formset.is_valid():
            post_form.save()
            image_formset.save()
            return redirect('posts:list')
    else:
        post_form = PostForm(instance=post)
        image_formset = ImageFormSet(instance=post) #post가 들고있는 모든 이미지(부모의 객체만 넘겨주면 부모가 들고있는 모든 사진을 다 가져옴)
    return render(request, 'posts/form.html', {'post_form':post_form, 'image_formset': image_formset},) #create.html에 updata 기능을 구현
    
def delete(request, post_id):
    # post = Post.objects.get(pk=post_id)
    post = get_object_or_404(Post, id=post_id) # 뭐가 있으면 데이터를 들고오고 없으면 404에러를 띄움 import 해줘야함
    
    if post.user != request.user: #post.user와 로그인된 유저 정보가 다르다면
        return redirect('post:list')
    
    post.delete()
    return redirect('posts:list')
    
# from django.views.decorators.http import require_POST  << POST 방식이 있다면 GET방식도 있음
@login_required #decorator가 여러개면 위에 decorator부터 실행
@require_POST # import 해줘야함   
def comment_create(request, post_id): # 댓글작성하는 테이블을 만드는게 아니라 포스트안에서 댓글이 작성되고나서 포스트 list로 리다이렉트
    # post = get_object_or_404(Post, id=post_id)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False) # 댓글에 담겨있는 모든 정보
        comment.user = request.user # 어떤사람이 작성했는지에 대한 정보
        comment.post_id = post_id # 앞에 post_id는 models.py에 Comment 클래스에 있는 post변수가 외래 키값으로 온 형태, 함수 인자값 post_id와는 다름
        # comment.post = post
        comment.save()
    # return redirect('posts:list')
    return JsonResponse({'id': comment.id, 'postId': post_id, 'username': comment.user.username, 'content': comment.content,})
    
@require_http_methods(['GET','POST']) #다양한 요청방식을 모두 허용    
def comment_delete(request, post_id, comment_id): #주소에 순서대로 인자값도 순서가 같게 id값을 줘야함
    comment = get_object_or_404(Comment, id=comment_id) #Comment를 import해와야함
    if comment.user != request.user: # 댓글적은 사람과 로그인한 사람이 다르다면 list로 돌려보냄
        return redirect('post:list')
    comment.delete() # 같은 사람이라면 댓글을 지우도록 함
    
    return redirect('posts:list')
@login_required #로그인 한 사람만 좋아요를 누를 수 있도록
def like(request, post_id): #좋아요 기능
    post = get_object_or_404(Post, id=post_id)
    
    if request.user in post.like_users.all(): #현재 post를 좋아요를 누른 user들 중에 현재 로그인한 유저가 있으면
    # 1. 좋아요 취소!
        post.like_users.remove(request.user)
        liked = False # 자바스크립에 대한 응답
    # 2. 좋아요
    else:
        post.like_users.add(request.user) # 현재 좋아요를 누른 포스트에 현재 로그인된 사람의 정보를 추가
        liked = True
    
    return JsonResponse({'liked': liked, 'count': post.like_users.count()}) #import 해야함
    # return redirect('posts:list') # 기존에 했던 방식
    