from django.urls import path
from apps.settings.views import index1,index2, index3

urlpatterns = [
    path('1', index1, name = 'index'),
    path('2', index3, name= 'index3'),
    path('', index2, name='index2')

]