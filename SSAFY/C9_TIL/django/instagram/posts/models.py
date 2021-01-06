from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.conf import settings  #settings.py에 있는 모든걸 쓸수있음.


def post_image_path(instance, filename):
    return 'posts/{}/{}'.format(instance.pk, filename)
    

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # 이부분 정리가 안됌 ㅠㅠ (CASCADE는 1에대한 옵션이 사라지면 그와관련된  N개 모두 삭제)
    # ForeignKey() 유저에 대한 모든 정보를 불러옴.
    content = models.TextField()
    # image = models.ImageField(blank=True) #blank True는 값이 안들어가도 좋다는 뜻, 이미지파일을 파이썬에서 다루기 위해서는 pip install pillow필요
    # image = ProcessedImageField(
    #     upload_to=post_image_path, # 저장 위치(함수를 호출하는게 아니라 함수 자체를 넘기는거임 '()'안넣어야함)
    #     processors=[ResizeToFill(600,600)], # 처리할 작업 목록
    #     format='JPEG', # 저장 포맷
    #     options={'quality':90}, #옵션
    #     )
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts') #좋아요를 구현하는 컬럼

class Image(models.Model): # Post에 있던 image=ProcessedImageField를 가지고옴
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    file = ProcessedImageField(
        upload_to=post_image_path, # 저장 위치(함수를 호출하는게 아니라 함수 자체를 넘기는거임 '()'안넣어야함) # 위에 함수로 지정함
        processors=[ResizeToFill(600,600)], # 처리할 작업 목록
        format='JPEG', # 저장 포맷
        options={'quality':90}, #옵션
        )    
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #유저랑  comment 1:N 관계
    post = models.ForeignKey(Post, on_delete=models.CASCADE) # ForeignKeym 는 무조건 1이 삭제됐을때 N관계에 있는 정보를 어떻게 처리할건지 알려저야함
    content = models.TextField()
    
