from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

def show_html(request):
    data = MyWatchList.objects.all()
    sudah = MyWatchList.objects.filter(watched='Sudah').count()
    belum = MyWatchList.objects.filter(watched='Belum').count()

    if sudah >= belum:
        msg = "Selamat, kamu sudah banyak menonton!"
    else:
        msg = "Wah, kamu masih sedikit menonton!"

    context = {
        'list_watchlist': data,
        'msg':msg
    }

    return render(request, 'mywatchlist.html', context)

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show(request):
    return HttpResponse("Halaman MyWatchList")