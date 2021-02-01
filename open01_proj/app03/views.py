from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
# Create your views here.
def home(request):
    return HttpResponseRedirect("0/static/index.html")