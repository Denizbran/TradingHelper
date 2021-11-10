from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,"index.html")

def haberler(request):
    return render(request,"haberler.html")

def kagitsec(request):
    return render(request,"kagitsec.html")

def tavsiye(request):
    return render(request,"tavsiye.html")

