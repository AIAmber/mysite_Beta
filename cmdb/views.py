from django.shortcuts import render
from django.shortcuts import HttpResponse
import datetime
# Create your views here.

def tangshi(request):
    # request.POST
    # request.GET
    #return HttpResponse("Hello, world!")
    return  render(request, 'tangshi.html')

def time(request):
    now = datetime.datetime.now()
    html = "<html> <body> It is now %s </body> </html>" % now
    return HttpResponse(html)
