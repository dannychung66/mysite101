from django.shortcuts import render
from django.http import HttpResponse 

def index(request):
   return render(request, "music/index.html", locals())

def detail(request):
   return render(request, "music/detail.html", locals())
