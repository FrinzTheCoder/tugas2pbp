from django.urls import path
from katalog.views import show_katalog

urlpatterns = [
    path('', show_katalog, name='show_katalog'),
]

# TODO: Implement Routings Here
