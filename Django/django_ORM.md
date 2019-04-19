### django 0417

* `pip freeze` : bash에서 이 명령어를 치면 pip로 설치된 프로그램을 볼 수 있다.
* `pip uninstall django` = 장고 잘못 설치했으면 uninstall하고 다시 만들기

## ORM

### 정리
* ```class Post ```  
  - **Django** - Model(장고에서는 Model),  
  - **Db** - Table(데이터베이스에서는 Table) 
* ```post :=Post() ```: 
  - **Django** - Instance or Object(Post 클래스의 인스턴스를 생성한다고 함)
  - **DB** - Record, Row

* ```title``` : 
  * **Django** - Field, 
  * **DB** - Column

* **마이그레이션**
  * ./manage.py makemigrations
  * ./manage.py migrate

* `pip install django_extensions`
  * Django shell 에서 불편한 부분을 개선해주는 확장 프로그램(원래는 수동으로 import를 다 해야하지만 확장프로그램을 설치하면 그 과정을 다 해준다.)
  * 설치 후 settings.py App 목록에 `django_extensions` 을 추가해줌 
  * 터미널에 `./manage.py shell_plus` 입력하고 실행

### CRUD(orm.models.py)

#### 1. Create

```shell
# shell

# 방법1
>>> post = Post(title='hello-1') #객체를 생성
>>> post.title
'hello-1'
>>> post.save() #데이터를 저장
>>> <Post: Post object (1)> 
# 저장하기 전에는 ()안에 None값이 들어갔으나 저장 한 후에는 데이터 id값이 들어간다.
>>> Post.objects # 장고 데이터를 관리하는 메서드들이 저장되있어.
<django.db.models.manager.Manager object at 0x7f47f448fcf8>

# 방법2(objects를 이용)
>>> post2 = Post.objects.create(title='hello-2') #create때문에 저장안해도 바로 저장됨
>>> post2
<Post: Post object (2)>

# 방법3
>>> post3.title='hello-3'
>>> post3.title
'hello-3'
>>> post3.save() # 저장해줘야함
>>> post3
<Post: Post object (3)>
>>> post3.title = 'hello!!!'
>>> post3.save() # 데이터 값을 수정하고 싶을때 

```



#### 2.  Read

```shell
# shell
# 1. All
>>> posts = Post.objects.all() # 이 코드가 실행되는 순간 장고는 database에서 데이터를 가져옴
# 모든 data를 변수에 저장할 때는 복수형으로 변수명 지정

# 2. One
# 방법1
>>> Post.objects.get(id=1) # 특정한 id값의 데이터를 가지고 오고 싶을때 (id대신 pk도 가능)
<Post: Post object (1)>
# 방법2
>>> Post.objects.get(title='hello-2') # 데이터 값으로 불러올 수도 있음
# 만약 타이틀이 같다면 id값이 작은 순으로 불러옴
# 방법3
>>> Post.objects.filter(title='hello') #title값이 'hello'인걸  아이디값 순으로 리스트로 가져옴
# 만약 title='hello' 가 여러개가 있다면 id값이 작은 순으로 리스트형태로 나옴.
>>> Post.objects.filter(title='hello')[0] # 리스트형태라서 인덱스 접근
>>> Post.objects.filter(title='hello').first() # 혹은 .first() 메서드 이용
# get은 값이 없으면 에러가 나지만 filter은 없으면 빈리스트로 나옴

# 3. Where(filter)
>>> posts = Post.objects.filter(title='hello-1')
>>> post = Post.objects.filter(title='hello-1').first() # 또는 [0]

# 4. LIKE
>>> Post.objects.filter(title__contains='lo')
# 특정 값이 포함된 데이터를 찾을때 

# 5. Order_by
>>> Post.objects.order_by('title') # title을 기준으로 오름차순으로 정렬
>>> Post.objects.order_by('-title') # title을 기준으로 내림차순으로 정렬
>>> Post.objects.filter(title__contains='hello').order_by('-id')
# title에 hello를 포함하고 있는 데이터를 아이디값 순으로 내림차순 정렬

# 6. offset & limit
>>> Post.objects.all()[0] #=> offset: 0 limit: 1
# 인덱스 접근 자체가 limit(뽑아오는 개수)가 1개란게 정해져있음
# offset은 앞에 데이터가 있는 수
>>> Post.objects.all()[1] #=> offset: 1 limit: 1
>>> Post.objects.all()[1:3] #=> offset: 1 limit: 2

*****결국 Post.objects.all()[offset:offset + limit]  ############# 시험문제!!!
```



#### 3. Update

```shell
#shell

# post = Post.objects.get(pk=1)
# post.title = 'hello-5'
# post.save() # 실제 데이터베이스에 저장
```



#### 4. Delete

```shell
# shell
>>> post = Post.objects.get(pk=1)
>>> post.delete()
>>> post.title
'hello=-1'
# 인스턴스 객체는 아직 그대로 남아있기 때문.
# 한줄로
>>> Post.objects.get(pk=1).delete()
```



### 1:N ORM(onetomany.models.py)

```python
class User(models.Model):
    name = models.TextField()
    
# User:Post = 1:N
class Post(models.Model):
    title = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # 이 포스터를 쓴 유저가 누구인지
    # User에 대한 정보가 키값(user_id)으로 들어감

# User:Comment = 1:N
# Post:Comment = 1:N
class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # 이 댓글은 쓴 유저가 누구인지
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # 이 댓글을 쓴 포스터가 누구의 포스터인지, 그리고 post에는 포스터를 쓴 유저의 정보가 있다.
```

```shell
user1 = User.objects.create(name="Kim")
user2 = User.objects.create(name="Lee")

#user정보를 가져올 때 객체 그대로 가져오는게 좋다.
post1 = Post.objects.create(title='1글', user=user1) or user_id=user1.id랑 같음
post2 = Post.objects.create(title='2글', user=user1)
post3 = Post.objects.create(title='3글', user=user2)

# 하나의 예를 들면 c1은 '1글1댓글'을 user1이 post1이란 글에 달았다.
c1 = Comment.objects.create(content='1글1댓글', user=user1, post=post1)
c2 = Comment.objects.create(content='1글2댓글', user=user2, post=post1)
c3 = Comment.objects.create(content='1글3댓글', user=user1, post=post1)
c4 = Comment.objects.create(content='1글4댓글', user=user2, post=post1)
c5 = Comment.objects.create(content='2글1댓글', user=user1, post=post2)
c6 = Comment.objects.create(content='1글5댓글', user=user2, post=post1)
c7 = Comment.objects.create(content='2글2댓글', user=user2, post=post2)

# 예시
# 1. 1번 사람이 작성한 게시글은?
 user1.post_set.all()

# 2. 1번 사람이 작성한 게시글의 댓글들을 출력하라
 for post in user1.post_set.all():
     for comment in post.comment_set.all():
         print(comment.content)

# 3. 2번 댓글을 쓴 사람의 유저
 c2.user
    
# 4. 2번 댓글을 쓴 사람이 작성한 게시글은?
 c2.user.post_set.all()

# 5. 1번 글의 첫번째 댓글을 쓴 사람의 이름은?
 post1.comment_set.first().user.name
 post1.comment_set.all()[0].user.name
 
# 6. '1글'이 제목인 게시글은?
 Post.objects.filter(title='1글')

# 7. 댓글 중에 해당 게시글의 제목이 1글인 것은?
# 방법 1
 Comment.objects.filter(post__title='1글')
# 방법 2
# post1 = Post.objects.get(title='1글')
 Comment.objects.filter(post=post1)

# 8. 댓글 중에 해당 게시글의 제목에 '1'이 들어가 있는 것은?
 Comment.objects.filter(post__title__contains='1')
 #모든 댓글에서 포스터, 제목에, 1이 포함되있는 데이터
 
```

 

### M:N ORM(manytomany.models.py)

```python
# 병원에 오는 사람들을 기록하는 시스템을 만들려고 한다.
# 필수적인 모델은 환자와 의사이다.
# 어떠한 관계로 표현할 수 있을까?

class Doctor(models.Model):
    name = models.TextField() # 의사정보

# Doctor:Patient = 1:N
class Patient(models.Model):
    name = models.TextField()
    doctors = models.ManyToManyField(Doctor, related_name='patients',through='Reservation') 
    # related_name은 patient_set.all()라고 불러와야하는 걸 patients.all()로 불러올수있음
    # 의사가 진료한 환자만 아는게 아니라 환자가 누구에게 진료받았는지 까지 같이 알 수 있게 하기위해
	# 환자와 의사를 M:N 관계를 맺게 하겠다.(Reservation을 통해서)
M:N 관계 방법 1. 
# Doctor:Reservation = 1:N  -> Reservation = N*Doctor
# Patient:Reservation = 1:M -> Reservation = M*Patient
# Doctor:Patient = M:N = Doctor:Patient
class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    
>>> doctor1 = Doctor.objects.create(name='Kim') 
>>> doctor2 = Doctor.objects.create(name='Kang')
>>> patient1 = Patient.objects.create(name='Tom')
>>> patient2 = Patient.objects.create(name='John')
# 예약 Object생성(1번의사가 2번환자를 진료)
# 이렇게하면 id값이 1인 의사와 id값이 2인 환자를 값으로 갖는 하나의 레코드가 생성됨
# 예약 객체 안에서 id값이 1인(아직 하나만 만들었으므로)
>>> Reservation.objects.create(doctor=doctor1, patient=patient2)
# 1번 의사가 진료한 환자를 가져오기
>>> for res in doctor1.reservation_set.all():
    	print(res.patient.name)
M:N 관계 방법 2.       
class Doctor(models.Model):
    name = models.TextField() # 의사정보
# Doctor:Patient = 1:N
class Patient(models.Model):
    name = models.TextField()
    doctors = models.ManyToManyField(Doctor, related_name='patients',)
>>> doctor1 = Doctor.objects.create(name='Kim')
>>> doctor2 = Doctor.objects.create(name='Kang')
>>> patient1 = Patient.objects.create(name='Tom')                                                                                                                            
>>> patient2 = Patient.objects.create(name='John')  
>>> doctor1.patients.all()
<QuerySet []>
    
>>> doctor1.patients.add(patient1)   # 1번 의사에 1번환자를 추가해줌
>>> doctor1.patients.all() # 1번이사의 모든 환자를 출력했을때
 <QuerySet [<Patient: Patient object (1)>]>
```

