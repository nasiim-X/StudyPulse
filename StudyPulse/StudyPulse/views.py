from django.contrib import messages
from django.shortcuts import redirect, render
from app.models import Categories,Course,Level,Video,UserCource
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.db.models import Sum

def BASE(request):
    return render(request,'base.html')


def HOME(request):
    category = Categories.objects.all().order_by('id')[0:5]
    course = Course.objects.filter(status = 'PUBLISH').order_by('-id')

    context = {
        'category':category,
        'course':course,
    }

    return render(request,'Main/home.html',context)

def SINGLE_COURSE(request):
    category = Categories.get_all_category(Categories)
    level = Level.objects.all()
    course = Course.objects.all()
    FreeCourse_count = Course.objects.filter(price = 0).count()
    PaidCourse_count = Course.objects.filter(price__gte=1).count()

    context = {
        'category' : category,
        'level' : level,
        'course' : course,
        'FreeCourse_count':FreeCourse_count,
        'PaidCourse_count':PaidCourse_count,
    }

    return render(request,'Main/single_course.html',context)

def filter_data(request):
    category = request.GET.getlist('category[]')
    level = request.GET.getlist('level[]')
    price = request.GET.getlist('price[]')
    
    if price == ['PriceFree']:
        course = Course.objects.filter(price=0)
    elif price == ['PricePaid']:
        course = Course.objects.filter(price__gte=1) 
    elif price == ['PriceAll']:
        course = Course.objects.all()
    elif category:
        course = Course.objects.filter(category__id__in = category).order_by('-id')
    elif level:
        course
    else:
        course = Course.objects.all().order_by('-id')
    
    context = {
        'course':Course.objects.filter(level__id__in = level).order_by('-id')
    }
    t = render_to_string('ajax/course.html',context)
    return JsonResponse({'data': t})

def CONTACT(request):
    category = Categories.get_all_category(Categories)

    context = {
        'category':category
    }
    return render(request,'Main/contact_us.html',context)

def ABOUT(request):
    category = Categories.get_all_category(Categories)

    context = {
        'category':category
    }
    return render(request,'Main/about_us.html',context)

def SEARCH_COURSE(request):

    category = Categories.get_all_category(Categories)

    query = request.GET['query']
    course = Course.objects.filter(title__icontains = query)

    context = {
        'course':course,
        'category':category
    }
    return render(request,'search/search.html',context)


def COURSE_DETAILS(request,slug):

    category = Categories.get_all_category(Categories)
    time_duration = Video.objects.filter(course__slug = slug).aaggregate(sum=Sum('time_duration'))

    course_id = Course.objects.get(slug = slug)
    try:
        check_enroll = UserCource.objects.get(user = request.user, course = course_id)
    except UserCource.DoesNotExist:
        check_enroll = None
       
    course = Course.objects.filter(slug = slug)

    if course.exists():
        course = course.first()
    else:
        return redirect('404')
    
    context = {
        'course':course,
        'category':category,
        'time_duration':time_duration,
        'check_enroll':check_enroll
    }
    return render(request,'course/course_details.html',context)


def PAGE_NOT_FOUND(request):

    category = Categories.get_all_category(Categories)

    context = {
        'category':category
    }
    return render(request,'error/404.html',context)


def CHECKOUT(request,slug):
    course = Course.objects.get(slug = slug)
    
    if course.price == 0:
        course = UserCource (
            user = request.user,
            course =course,
        )
        course.save()
        messages.success(request, 'Course is Successfully Enrolled !')
        return redirect('my_course')
    
    return render(request,'checkout/checkout.html')

def MY_COURSE(request):
    course = UserCource.objects.filter(user = request.user)

    context = {
        'course':course,
    }
    return render(request,'course/my_course.html',context)