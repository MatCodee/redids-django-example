from django.shortcuts import render
from .models import Books
from django.core.cache import cache
from django.conf import settings


#CACHE_TTL = getattr(settings, 'CACHE_TTL',timeout=25)

# Create your views here.
def home(request):
    context = {}
    context['books'] = Books.objects.all()
    return render(request,'home.html',context)


def detail(request,id):
    context = {}
    if cache.get(id):
        context['book'] = cache.get(id)
        print("DATA FROM CACHE")
    else:
        context['book'] = Books.objects.filter(pk=id).first()
        cache.set(id,context['book'])
        print("DATA FROM DB")
    return render(request,'detail.html',context)