from django.urls import path
from . import views

urlpatterns = [
    path('help/<path:slug>', views.FeedBackForm.as_view(), name='feedback'),
]
