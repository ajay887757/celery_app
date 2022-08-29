from http.client import HTTPResponse
from django.shortcuts import render
from .task import test_func

# Create your views here.

def test(request):
    test_func.delay()
    return HTTPResponse("View Done")