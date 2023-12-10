from django.contrib import admin
from django.urls import path
from apps.settings.views import index, index2,index3,index4

urlpatterns = [
     path('', index,name='index'),
     path('about/', index2,name='index2'),
     path('blog/', index3,name='index3'),
     path('index/', index4,name='index4')
]