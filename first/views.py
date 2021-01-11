from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from datetime import datetime

import random

def index(request):
    now=datetime.now()
    context={
        'current_date':now
    }
    return render(request,'first/index.html',context)




def select(request):
    context={}
    return render(request,'first/select.html',context)


def result(request):
    chosen=int(request.GET['number'])




    context={
        'number': chosen
    }


    return render(request,'first/result.html',context)
