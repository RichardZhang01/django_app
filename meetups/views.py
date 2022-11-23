from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Django invokes this function automatically
def index(request):
    return HttpResponse('Hello World')