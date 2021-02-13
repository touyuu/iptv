from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.shortcuts import redirect

from phoenix.phoenix_show import PhoenixShow


def index(request, name):
    #return HttpResponse("Hello, world. You're at the polls index.")

    s = PhoenixShow(name)
    return redirect(s.get_real_url(), permanent=True)

