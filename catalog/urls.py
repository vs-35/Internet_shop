from django.urls import path

from catalog.views import index, home

urlpatterns = [
    path('', index, name='index'),
    path('', home, name='home'),
]