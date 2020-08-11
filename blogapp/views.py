from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog


# Create your views here.
def home(request):

    # return HttpResponse("Hello, Django")
    return render(request, "blogapp/home.html")








