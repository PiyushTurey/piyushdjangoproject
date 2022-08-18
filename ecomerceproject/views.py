from django.shortcuts import render

from math import ceil
# import the logging library

# Create your views here.
from django.http import HttpResponse

def index(request):

    return render(request, 'index.html')