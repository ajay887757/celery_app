from django.shortcuts import render
from django.http import HttpResponse
from .task import test_func
import logging

#now we will Create and configure logger 
logging.basicConfig(filename="celeryData.log", 
					format='%(asctime)s %(message)s', 
					filemode='a') 

logger=logging.getLogger() 
logger.setLevel(logging.DEBUG) 
# Create your views here.

def test(request):
    test_func.delay()
    logger.debug("This is From View.py") 
    return HttpResponse("View Done")