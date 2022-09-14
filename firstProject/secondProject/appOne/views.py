from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):

    return render(request, 'sites/index.html',{
        'title': 'Inicio'
    })


def about(request):

    return render(request, 'sites/about.html', {
        'title': 'Sobre nosotros'
    })