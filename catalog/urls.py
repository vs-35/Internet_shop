from django.urls import path

from catalog.views import index, home

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', index, name='index'),
]