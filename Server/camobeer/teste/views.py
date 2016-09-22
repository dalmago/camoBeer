from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    html = "<DOCTYPE html>\r\n<html><head><title>Teste</title></head><body>"
    html += "Hello World!<br><img src=\"/static/temps.png\" height=\"600p\"></body></html>"
    return HttpResponse(html)
