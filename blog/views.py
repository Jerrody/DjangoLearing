from django.shortcuts import render
from django.views.generic import View

from .models import Category, Post


# Category
class HomeView(View):
    def get(self, request):
        category_list = Category.objects.all()
        post_list = Post.objects.all()
        return render(request, 'blog/home.html', {'categories': category_list, 'posts': post_list})


class CategoryView(View):
    def get(self, request, slug):
        category = Category.objects.get(slug=slug)
        return render(request, 'blog/post_list.html', {'category': category})


class PostView(View):
    def get(self, request, slug):
        post_list = Post.objects.get(slug=slug)
        return render(request, 'blog/post_page.html', {'post': post_list})
