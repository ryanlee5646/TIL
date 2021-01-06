from django.shortcuts import render

# Create your views here.
def hello(request):
    return render(request, 'hello.html', {})
    
def hi(request, apple):
    print(apple)
    return render(request, 'hi.html', {'apple':apple})