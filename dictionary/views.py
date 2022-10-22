from re import search
from django.shortcuts import render
from PyDic

# Create your views here.
def index(request):
    return render(request,'index.html')

def word(request):
    search = request.GET.get('search')
    return render(request,'word.html')