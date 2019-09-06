from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

import os
#import django_dev_commands
import cgi, cgitb


def formpage(request):
    return render(request,"form.html")
def form(request):
    if (request.method=="POST"):
        val1 = request.FILES["fileToUpload"]
        val2 = request.FILES["fileToUploa"]
        fs=FileSystemStorage()
        name1=fs.save(val1.name,val1)
        context1=fs.url(name1)
        name2 = fs.save(val2.name, val2)
        context2 = fs.url(name2)
        print("name of pic 1---",name1)
        print("stored in----",context1)
        print("pic 1 recognized by----",val1.name)
        print("size of pic1----",val1.size)
        print("name of pic 1---",name2)
        print("stored in----",context2)
        print("pic 1 recognized by",val2.name)
        print("size of pic2",val2.size)

    return render(request,"forum.html",{"value1as":val1,"context1as":context1,"value2as":val2,"context2as":context2})