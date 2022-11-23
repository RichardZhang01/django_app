from django.shortcuts import render

# Create your views here.

# Django invokes this function automatically


def index(request):
    return render(request, 'meetups/index.html')
