from django.urls import path
from blog.views import HomeView

from . import views

urlpatterns = [
    path('', views.HomeView.as_view()),
    path('<slug:slug>/', views.CategoryView.as_view(), name='category'),
    path('<slug:slug>/', views.PostView.as_view(), name='post'),
]
