from django.shortcuts import render
from django.http import HttpResponse


def loadIndex(request):
    return render(request, 'pages/index.html')


