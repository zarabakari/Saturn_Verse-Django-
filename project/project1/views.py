from django.shortcuts import render
from django.http.response import HttpResponse


def home(request):
    return HttpResponse ("<h1>hello </h1>")

def preview1(request):
    return HttpResponse ("<h1>welcome</h1>")


def preview2(request):
    return HttpResponse ("<h1>your teacher is mr desmond</h1>")


def preview3(request):
    return HttpResponse ("<h1>we are learning django</h1>")

def preview4(request):
    return HttpResponse ("<h1>bye</h1>")








