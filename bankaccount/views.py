from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
def home(request):
    x='<h1>Welcome to My Website</h1>'
    return HttpResponse (x)

def contact(request):
    x='<h1>My Contact number is : 7858960123</h1>'
    return HttpResponse (x)

def services(request):
    x='<h1>We provide all types of services</h1>'
    return HttpResponse (x)