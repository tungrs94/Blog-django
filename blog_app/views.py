# Create your views here.
from django.shortcuts import render


def home(request):
    return render(request, 'homepage/home.html')


def thongtin(request):
    return render(request, 'homepage/thongtin.html')
