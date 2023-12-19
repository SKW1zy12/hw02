from django.urls import path
from apps.settings.views import index,blog_detail

urlpatterns = [
    path('', index, name='index'),
    path('blog_detail/<int:id>/', blog_detail, name='blog_detail'),
]