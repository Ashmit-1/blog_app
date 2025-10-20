from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name="blog"),
    path('create_post/', views.create_post, name="create_post"),
] 