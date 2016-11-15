# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 15:06:27 2015

@author: 105028218
"""
import requests
import os
import shutil

global dump

def download_file():
    global dump
    url = "http://blogs.geoilandgas.com/accessknowledge/wp-content/uploads/sites/99/2014/08/PowerPoint-Slide-Show-AK-BAnner2.pptx_-300x110.jpg"
    file = requests.get(url, stream=True)
    dump = file.raw

def save_file():
    global dump
    location = os.path.abspath("C:\folder\filegz")
    with open("filegz", 'wb') as location:
        shutil.copyfileobj(dump, location)
    del dump
