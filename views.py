# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 20:23:58 2020

@author: LENOVO
"""

from django.shortcuts import render
from django.contrib import messages
import csv,io


def profile_upload(request):

    template = "profile_upload.html"
    data = Profile.objects.all()

    prompt = {
        'order': 'Order of the CSV should be medName,manufacturer,onemg_price,Ingredients',
        'profiles': data
              }

    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')

io_string = io.StringIO(data_set)
next(io_string)
for column in csv.reader(io_string, delimiter=',', quotechar="|"):
    _, created = Profile.objects.update_or_create(
        medName=column[0],
        manufacturer=column[1],
        onemg_price=column[2],
        Ingredients=column[3],

    )
context = {}
return render(request, template, context)

