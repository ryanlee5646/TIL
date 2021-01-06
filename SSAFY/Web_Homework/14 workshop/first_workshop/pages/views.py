from django.shortcuts import render

# Create your views here.
def info(request):
    return render(request, 'info.html')
def information(request, name):
    class_age = {'이규진': 29, '진민재': 28, '강대현': 28, '윤종원': 26, '이현수': 30,
    '서민수': 28, '조영현': 38}
    return render(request, 'information.html', {'name': name, 'age': class_age[name]})