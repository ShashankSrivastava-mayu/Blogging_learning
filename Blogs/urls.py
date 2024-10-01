from .import views
from django.urls import path


urlpatterns = [
  path("", views.blogs_one, name = "blogs_one"),
  path("blogs_posts", views.blogs_post,name = "blogs_post"),
  path("blogs_post/<slug:slug>", views.blogs_post_details,name = "blogs_post_details")
]