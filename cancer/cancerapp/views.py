from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render
import statistics
from datetime import date
import math
from django.core.files.storage import default_storage

import tensorflow as tf
from tensorflow.keras.preprocessing import image
import tensorflow.keras
import cmath
from tensorflow.keras.models import load_model
import numpy as np

# Create your views here.
def home(request):
    return render(request,'predict.html')

def predict(request):
    a=request.FILES['img']
    model = load_model("static/model/model.hdf5")
    classes_dir = [1,2,3]
    file_name="pic.jpg"
    file_name2=default_storage.save(file_name,a)
    file_url=default_storage.url(file_name2)
    img = image.load_img(file_url, target_size=(350,350))
    norm_img = image.img_to_array(img)/255
    input_arr_img = np.array([norm_img])
    pred = np.argmax(model.predict(input_arr_img))
    print(model.predict(input_arr_img))
    print(classes_dir[pred])
    m=classes_dir[pred]
    if(m==1):
         return render(request,'adeno.html',{'num': m})
    elif(m==3):
        return render(request,'sqa.html',{'num': m})
    else:
        return render(request,'normal.html',{'num': m})

def info(request):
    return render(request,'info.html')
def about(request):
    return render(request,'about.html')