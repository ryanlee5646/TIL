from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.TextField()
    
# 정리
# class Post : 
# Django - Model(장고에서는 Model) 
# Db - Table(데이터베이스에서는 Table) 
# post = Post() : Django - Instance or Object(Post 클래스의 인스턴스를 생성한다고 함)

# CRUD
# 1. Create
# 방법 1
# post1 = Post(title='hello-1')
# post1.save()

# 방법 2
# post2 = Post.objects.create(title='hello-2')

# 방법3
# post3 = Post()
# post3.title='hello-3'
# post3.save() # 저장해줘야함

# 2. Read
# 2-1. All
# posts = Post.object.all()

#2-2. One
# 방법 1
# post = Post.objects.get(pk=1) # id=1, title = 'hello-1'도 가능

# 방법 2(views.py 한정)
# from django.shortcuts import get_objects_or_404
# post = get_object_or_404(Post, pk=1)

# 2-3 Where(filter)
# posts = Post.objects.filter(title='hello-1')
# post = Post.objects.filter(title='hello-1').first() # 또는 [0]

# 4. LIKE
# Post.objects.filter(title__contains='lo')
# 특정 값이 포함된 데이터를 찾을때 

# 5. Order_by
# Post.objects.order_by('title') # title을 기준으로 오름차순으로 정렬
# Post.objects.order_by('-title') # title을 기준으로 내림차순으로 정렬

# 6. offset & limit

# Post.objects.all()[0] #=> offset: 0 limit: 1
# Post.objects.all()[1] #=> offset: 1 limit: 1