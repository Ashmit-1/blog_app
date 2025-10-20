from django.shortcuts import render
from .forms import BlogForm
from .models import Blog

# Create your views here.
def blog(request):
    all_blogs = Blog.objects.all()
    return render(request, "blog_app/index.html", {"all_blogs" : all_blogs})