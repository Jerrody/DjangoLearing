from django.urls import path

from . import views

urlpatterns = [
    path('tag/<slug:slug>/', views.PostListView.as_view(), name='tag'),
    path(
        '<slug:category_slug>/',
        views.PostListView.as_view(),
        name='category'
    ),
    path(
        '<slug:category>/<slug:slug>/',
        views.PostDetailView.as_view(),
        name='post_detail'),
    path('', views.PostListView.as_view()),
]
