from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('<h1> This is the FIRST Sring format response</h1>')
def second(request):
    return HttpResponse('<h1> This is the SECOND string format responmse</h1>')
def third(request):
    return HttpResponse('<h1> This is the THIRD Sring format response</h1>')
def fourth(request):
    return HttpResponse('<h1> This is the FOURTH string format responmse</h1>')