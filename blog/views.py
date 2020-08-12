from datetime import datetime

from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import View

from .models import Category, Post
from .forms import CommentForm


class PostListView(View):
    """Category View"""
    def get_queryset(self):
        return Post.objects.filter(
            published_date__lte=datetime.now(),
            published=True
        )

    def get(self, request, category_slug=None, slug=None):
        category_list = Category.objects.filter(published=True)
        if category_slug is not None:
            posts = self.get_queryset().filter(
                category__slug=category_slug, category__published=True
            )
        elif slug is not None:
            posts = self.get_queryset().filter(tags__slug=slug)
        else:
            posts = self.get_queryset()
        if posts.exists():
            template = posts.first().get_category_template()
        else:
            template = 'blog/post_list.html'
        return render(
            request,
            template,
            {'post_list': posts, 'categories': category_list}
        )


class PostDetailView(View):
    """Full Post View"""
    def get(self, request, **kwargs):
        category_list = Category.objects.filter(published=True)
        post = get_object_or_404(Post, slug=kwargs.get('slug'))
        form = CommentForm()
        return render(
            request,
            post.template,
            {'categories': category_list, 'post': post, 'form': form}
        )

    def post(self, request, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post = Post.objects.get(slug=kwargs.get('slug'))
            form.author = request.user
            form.save()
        return redirect(request.path)
