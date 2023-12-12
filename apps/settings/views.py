from django.shortcuts import render

# Create your views here.
def index1(request):
    return render(request, 'blog-post.html', locals())

def index2(request):
    return render(request, 'index-slideshow.html', locals())

def index3(request):
    return render(request, 'blog.html', locals())