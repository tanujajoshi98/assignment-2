from django.shortcuts import render, loader
from django.http import HttpResponse, JsonResponse

from django.views import View
import datetime

# Create your views here.
def home(request):
    #return render(request,"home.html")
    today = datetime.datetime.now().date()
    return render(request,"home.html",{"tdate":today})

def add(request):

    val1 = float( request.GET['num1'])
    val2 = float(request.GET['num2'])
    res = val2/(val1**2)

    return render(request,"result.html",{'result':res})