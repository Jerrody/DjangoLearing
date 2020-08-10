from django.urls import path

from . import views

urlpatterns = [
    path('tag/<slug:slug>/', views.TagView.as_view(), name='tag'),
    path('<slug:category>/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('<slug:category_slug>/', views.CategoryView.as_view(), name='category'),
    path('', views.HomeView.as_view()),
]
