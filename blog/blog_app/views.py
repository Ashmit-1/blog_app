from django.shortcuts import render, redirect, get_object_or_404
from .forms import BlogForm
from .models import Blog

# Create your views here.
def blog(request):
    all_blogs = Blog.objects.all().order_by('-thumbnail')
    return render(request, "blog_app/index.html", {"all_blogs" : all_blogs})

def create_post(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user 
            post.save()
            return redirect('blog')
    else:
        form = BlogForm()
    return render(request, "blog_app/post_form.html", {"form" : form})

def edit_post(request, form_id):
    post = get_object_or_404(Blog, pk=form_id, user=request.user)
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user 
            post.save()
            return redirect('blog')
    else:
        form = BlogForm(instance=post)
    return render(request, "blog_app/post_form.html", {"form" : form})

def delete_post(request, form_id):
    post = get_object_or_404(Blog, pk=form_id, user=request.user)
    if request.method=="POST":
        post.delete()
        return redirect('blog')
    return render(request, 'blog_app/confirm_delete.html', {"post" : post})

