from django.shortcuts import render

# Create your views here.
def blog(request):
    return render(request, "blog_app/index.html")