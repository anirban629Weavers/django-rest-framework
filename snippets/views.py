from django.shortcuts import render
from django.http import JsonResponse
from .utils import *

def checkUtils(request):
    data1=check1()
    data2=check2()
    data3=check3()
    # return JsonResponse(data1,status=200,safe=False)
    return JsonResponse(data3,status=200,safe=False)
 