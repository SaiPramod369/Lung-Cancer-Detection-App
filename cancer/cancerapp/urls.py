from xml.etree.ElementInclude import include
from . import views
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
   path('home.html/',views.home),
   path('home.html/predict',views.predict),
   path('info.html/',views.info),
   path('about.html/',views.about)

]
