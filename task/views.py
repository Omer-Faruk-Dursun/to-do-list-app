from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("This is the index page !")

def task_view(request):
    return HttpResponse("This is the task page ! \n Hello world !")
