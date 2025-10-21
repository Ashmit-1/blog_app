from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import BlogForm, UserRegistraionForm
from .models import Blog

# Create your views here.
def blog(request):
    all_blogs = Blog.objects.all().order_by('-thumbnail')
    return render(request, "blog_app/index.html", {"all_blogs" : all_blogs})

@login_required
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

@login_required
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

@login_required
def delete_post(request, form_id):
    post = get_object_or_404(Blog, pk=form_id, user=request.user)
    if request.method=="POST":
        post.delete()
        return redirect('blog')
    return render(request, 'blog_app/confirm_delete.html', {"post" : post})



def register(request):
    if request.method=="POST":
        form = UserRegistraionForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('blog')
    else:
        form = UserRegistraionForm()
    return render(request, "registration/register.html", {"form" : form})