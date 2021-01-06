from django.shortcuts import render, redirect
from .models import Page

def new(request):
    return render(request, 'new.html')
    
def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    
    page = Page(title=title, content=content)
    page.save()
    
    return redirect('pages:detail', page.pk)

def index(request):
    pages = Page.objects.all()
    return render(request, 'index.html', {'pages':pages})
    
def detail(request, page_id):
    page = Page.objects.get(pk=page_id)
    return render(request, 'detail.html', {'page':page})
    
def delete(request, page_id):
    page = Page.objects.get(pk=page_id)
    page.delete()
    return redirect('pages:list')
    