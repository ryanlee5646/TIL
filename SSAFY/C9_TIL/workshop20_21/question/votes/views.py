from django.shortcuts import render, redirect
from .models import Question, Choice

# Create your views here.
def menu(request):
    question = Question.objects.first()
    choices = question.choice_set.all()
    return render(request, 'menu.html', {'question':question, 'choices':choices})
    