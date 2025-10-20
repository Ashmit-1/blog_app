from django.shortcuts import render, redirect
from .forms import BlogForm
from .models import Blog

# Create your views here.
def blog(request):
    all_blogs = Blog.objects.all().order_by('-thumbnail')
    return render(request, "blog_app/index.html", {"all_blogs" : all_blogs})

def create_post(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        print("POST request received Block")
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user 
            post.save()
            print("Redirect Block")
            return redirect('blog')
    else:
        form = BlogForm()
    return render(request, "blog_app/post_form.html", {"form" : form})