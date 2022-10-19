from django.shortcuts import render
from django.http import HttpResponse


def Me(request):
    return HttpResponse('Semangat Lisaa')


