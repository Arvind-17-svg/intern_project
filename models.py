# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 20:13:31 2020

@author: LENOVO
"""


from django.db import models

class Medapp(models.Model):
    medName=models.CharField(max_length=1000)
    manufacturer=models.CharField(max_length=1000)
    onemg_price=models.IntegerField(max_length=1000)
    ingredients=models.CharField(max_length=1000)
    