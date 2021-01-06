from django.shortcuts import render, redirect
from .models import Student
# Create your views here.

def new(request): # new.html은 새로운 정보를 입력하는 창
    return render(request, "new.html") 

def index(request): # 모든 학생 정보가 보이는 페이지
    students = Student.objects.all()
    return render(request, "index.html", {"students":students})
    
def create(request):
    name = request.POST.get("name")
    email = request.POST.get("email")
    birthday = request.POST.get("birthday")
    age = request.POST.get("age")
    
    student = Student(name=name, email=email, birthday=birthday, age=age)
    student.save() #데이터베이스에 저장
    return redirect(f"/student/{student.pk}/")

def detail(request, student_id):
    student = Student.objects.get(pk=student_id)
    return render(request, 'detail.html', {'student': student})
    
def delete(request, student_id):
    student = Student.objects.get(pk=student_id)
    student.delete()
    return redirect('/student/')

def edit(request, student_id):
    student = Student.objects.get(pk=student_id)
    return render(request, 'edit.html', {'student':student})
    
def update(request, student_id):
    student = Student.objects.get(pk=student_id)
    student.name = request.POST.get('name')
    student.email = request.POST.get('email')
    student.birthday = request.POST.get('birthday')
    student.age = request.POST.get('age')
    student.save()
    return redirect(f'/student/{student_id}')
    
