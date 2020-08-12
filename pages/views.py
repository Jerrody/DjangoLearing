from django.shortcuts import get_object_or_404, render
from django.views.generic import View

from .models import Page


class PageView(View):
    """Page View"""
    def get(self, request, **kwargs):
        post = get_object_or_404(Page, slug=kwargs.get('slug'))
        # unresolved: post.template(need to add page.template
        # or keep it how it is
        return render(request, post.template, {'post': post})
