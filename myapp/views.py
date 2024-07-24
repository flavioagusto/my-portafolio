from django.shortcuts import render
from .models import Blog

# Create your views here.

def blog(request):
    blog_data = Blog.objects.all()
    main_data = {"blog": blog_data}
    return render(request, "blog.html", main_data)

def home(request):
    return render(request, "home.html")
    