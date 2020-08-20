from django.urls import path

from . import views

urlpatterns = [
    # path('page/<slug:slug>', views.PageView.as_view(), name='about'),
    path('tag/<slug:slug>/', views.PostListView.as_view(), name='tag'),
    path(
        '<slug:category>/<slug:slug>/',
        views.PostDetailView.as_view(),
        name='post_detail'),
    path(
        '<slug:category_slug>/',
        views.PostListView.as_view(),
        name='category'
    ),
    path('', views.PostListView.as_view()),
]
