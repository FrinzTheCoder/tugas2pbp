from django.urls import path
from mywatchlist.views import *

urlpatterns = [
    path('html', show_html, name='show_html'),
    path('xml', show_xml, name='show_xml'),
    path('json', show_json, name='show_json'),
    path('', show, name='show')
    ]