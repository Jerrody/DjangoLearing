# from datetime import datetime
#
# from django.shortcuts import get_object_or_404, render
# from django.views.generic import View
#
# from .models import Page
#
#
# class PageView(View):
#     """Page View"""
#     def get(self, request, **kwargs):
#         page = Page.objects.filter(
#             published_date__lte=datetime.now(),
#             published=True)
#         # unresolved: post.template(need to add page.template
#         # or keep it how it is
#         return render(request, page.template, {'page': page})
