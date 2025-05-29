from django.urls import path
from . import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("posts/", views.posts),
    path("posts/<slug:slug>", views.post_detail, name="post-detail"),
    path("autors/", views.autors),
    path("autors/<int:id>", views.author_detail, name="author-detail"),
    path("tags/", views.tags),
    path("tags/<slug:slug>", views.tag_detail, name="tag-detail")
    ]