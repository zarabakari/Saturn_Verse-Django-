from django.shortcuts import render
from django.http.response import HttpResponse


def home(request):
    return HttpResponse ("<h1>1</h1>")

def preview1(request):
    return HttpResponse ("<h1>2</h1>")


def preview2(request):
    return HttpResponse ("<h1>3</h1>")


def preview3(request):
    return HttpResponse ("<h1>4</h1>")

def preview4(request):
    return HttpResponse ("<h1>5</h1>")








