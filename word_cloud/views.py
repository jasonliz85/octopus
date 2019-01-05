from django.shortcuts import render


from django.http import HttpResponse


def index(request):
    return HttpResponse("I am at the index()")

def results(request):
    return HttpResponse("I am at the results()")

