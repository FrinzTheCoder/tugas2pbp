from django.shortcuts import render
from katalog.models import CatalogItem

def show_katalog(request):

    data_katalog = CatalogItem.objects.all()

    context = {
        'list_katalog': data_katalog,
        'nama': 'Muhammad Falensi Azmi',
        'npm': '2106630334',
    }

    return render(request, "katalog.html", context)

# TODO: Create your views here.
