from django.shortcuts import render
import random
# Create your views here.
def index(request):
    return render(request, 'index.html')
# Template variable (html에 변수를 넘기는 것)    
def dinner(request):
    menu = ["피자", "족발", "햄버거", "안먹고 볼링침"]
    pick = random.choice(menu)
    return render(request, 'dinner.html', {'dinner': pick})
    
# Variable routing
def hello(request, name):
    return render(request, 'hello.html', {'name': name})

#Practice    
def identify(request, name):
    identity = ["더러움","깨끗함","천사","좋음","완벽주의자",
    "좋지않음","게으름"]
    pic = random.choice(identity)
    return render(request, 'identify.html', {'name': name, 'identify': pic})
    
# Form tag
def throw(request):
    return render(request, 'throw.html')
def catch(request):
    message = request.GET.get('message')
    return render(request, 'catch.html', {'m': message})
    
# Form 외부로 요청
def naver(request):
    return render(request, 'naver.html')
    
# Bootstrap 호출
def bootstrap(request):
    return render(request, 'bootstrap.html')