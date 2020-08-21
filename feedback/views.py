from django.shortcuts import redirect
from .models import FeedBackForm
from django.views.generic import View


class FeedBackForm(View):
    def post(self, request, **kwargs):
        form = FeedBackForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.full_name = request.user
            form.save()
        return redirect('/feedback/')
