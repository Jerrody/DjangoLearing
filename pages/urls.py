from django.urls import path

from . import views

urlpatterns = [
    path('<slug:slug>', views.PageView.as_view(), name='page_view')
]
