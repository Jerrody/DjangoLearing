from django.shortcuts import render
from django.views.generic import View
from datetime import datetime

from .models import Category, Post, Comment, Tag


# Category
class HomeView(View):
    """Trash Template"""
    def get(self, request):
        category_list = Category.objects.all()
        post_list = Post.objects.filter(published_date__lte=datetime.now(), published=True)
        return render(request, 'blog/post_list.html', {'categories': category_list, 'post_list': post_list})

class PostDetailView(View):
    """Full Post View"""
    def get(self, request, category, slug):
        category_list = Category.objects.all()
        post = Post.objects.get(slug=slug)
        comments = Comment.objects.filter(post_id=post)
        return render(request, post.template, {'categories': category_list, 'post': post, 'comments': comments})

class CategoryView(View):
    """Category View"""
    def get(self, request, category_slug):
        posts = Post.objects.filter(
            category__slug=category_slug, category__published=True, published=True
        )
        return render(request, posts.first().get_category_template(), {'post_list': posts})

class TagView(View):
    """Tag View"""
    def get(self, request, slug):
        posts = Post.objects.filter(tags__slug=slug)
        return render(request, posts.first().get_category_template(), {'post_list': posts})
