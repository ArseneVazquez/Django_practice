from django.urls import path
from . import views

urlpatterns = [
    path("", views.index.as_view(), name="starting-page"),
    path("posts", views.AllPost.as_view(), name="post-page"),
    path("posts/<slug:slug>", views.PostDetail.as_view(), name="post-detail-page"),
    path("read-later", views.ReadLaterView.as_view(), name="read-later")
]