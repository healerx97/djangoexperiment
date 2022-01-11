from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def sample_view(*args, **kwargs):
    return HttpResponse('<h1>Hello World</h1>')
