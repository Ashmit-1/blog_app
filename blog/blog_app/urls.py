from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name="blog"),
    path('create_post/', views.create_post, name="create_post"),
    path('<int:form_id>/edit_post/', views.edit_post, name="edit_post"),
    path('<int:form_id>/delete_post/', views.delete_post, name="delete_post"),

] 