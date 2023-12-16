from django.shortcuts import render
from apps.settings.models import Slide, Settings, About_me, Mentor,Card,Friend,Teacher,Blogpost, Mypro,Mytpoject
# Create your views here.
def index(request):
    slide = Slide.objects.all()
    logoo = Settings.objects.latest('id')
    me_about = About_me.objects.latest('id')
    mentor = Mentor.objects.latest('id')
    card = Card.objects.all()
    friend = Friend.objects.all()
    zaebalo = Teacher.objects.all()
    blog  = Blogpost.objects.all()
    my = Mypro.objects.latest('id')
    myproject = Mytpoject.objects.all()
    return render(request, 'index-slideshow.html', locals())

def blog(request):
    return render(request, 'blog.html', locals())

def blog_detail(request, id):
    blog = Blogpost.objects.get()
    return render(request,'blog-post.html', locals() )