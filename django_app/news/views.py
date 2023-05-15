from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def main(request):
    return HttpResponse('Главная страница')

def index(request):
    return HttpResponse('Hello world!')

def test(request):
    return HttpResponse('<h1>Тестовая страница</h1>')
