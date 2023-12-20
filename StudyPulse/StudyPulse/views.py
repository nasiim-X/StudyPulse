from django.shortcuts import redirect, render
from app.models import Categories


def BASE(request):
    return render(request,'base.html')


def HOME(request):
    category = Categories.objects.all().order_by('id')[0:5]

    context = {
        'category':category,
    }

    return render(request,'Main/home.html',context)

def SINGLE_COURSE(request):
    return render(request,'Main/single_course.html')

def CONTACT(request):
    return render(request,'Main/contact_us.html')

def ABOUT(request):
    return render(request,'Main/about_us.html')