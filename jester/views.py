from django.shortcuts import render
from django.http import HttpResponse

def landing_page(request):
    return HttpResponse("<h1>Bienvenido a Jester</h1><p>Landing page en construcción 🚀</p>")
