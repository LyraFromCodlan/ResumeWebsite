from django.urls import path
from . import views

urlpatterns = [
    path("", views.returnMainPage, name = "mainPage"),
    path("bar",views.sidebar, name="Sidebar"),
    path("post_list", views.posts, name="Posts")
]