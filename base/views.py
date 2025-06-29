# views.py
from django.shortcuts import render

def base(request):
    return render(request, 'base/base.html')

def base2(request):
    return render(request, 'base/base2.html')

def sobre(request):
    return render(request, 'base/sobre.html')
