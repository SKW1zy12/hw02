from django.contrib import admin
from django.urls import path
from apps.settings.views import index, index2,index3

urlpatterns = [
     path('index/', index,name='index'),
     path('blog/', index2,name='index2'),
     path('', index3,name='index3'),
]