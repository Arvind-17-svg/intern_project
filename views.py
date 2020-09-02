# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 20:23:58 2020

@author: LENOVO
"""

from django.shortcuts import render
from django.contrib import messages
import csv,io
import request

template='intern_upload.html'
data=Medapp.objects.all()

prompt={'order':'order should be medName,manufacturer,onemg_price,ingredients','profiles':data}

if request.method=='GET':
    return render(request,template,prompt)




csv_files=request.FILES['file']
if not csv_files.name.endswith('.csv'):
    messages.error("this is not a csv file")


data_set=csv_files.read().decode('UTF_8')
io_string=io.StringIo(data_set)
next(io_string)

for column in csv.reader(io_string,delimiter='',quotechar='|'):
    _,created=Medapp.objects.update_or_create(medName=column[0],
                                              manufacturer=column[1],
                                              onemg_price=column[2],
                                              ingredients=column[3])
context={}
return render(request,template,context)

