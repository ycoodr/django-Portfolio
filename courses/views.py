from django.shortcuts import render
from django.http import HttpResponse
from .models import Course

def index(request):
    courses = Course.objects
    return render(request, 'courses/index.html', {'courses': courses})

# Create your views here.
