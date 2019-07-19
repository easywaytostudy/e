from django.shortcuts import render, redirect
from .models import SummerCamp
from django.db.models import Max
# Create your views here.


def home(request):
    return render(request, 'home.html')


def contact_us(request):
    return render(request, 'contact_us.html')


def about_us(request):
    return render(request, 'about_us.html')


def winner(request):
    data = SummerCamp.objects.all().order_by('-marks')[:3]
    return render(request, 'winner.html', {'data':data})


def students(request):
    data = SummerCamp.objects.all()
    return render(request, 'students.html', {'data':data})


def crayon_rubbing_art(request):
    data = SummerCamp.objects.filter(game_name='crayon_rubbing_art')
    return render(request, 'crayon_rubbing_art.html', {'data':data})


def register(request):
    if request.method=='POST':
        student_name = request.POST.get('name')
        class_name = request.POST.get('class')
        school_name = request.POST.get('school')
        game_name = request.POST.get('game')

        data = SummerCamp(student_name=student_name, class_name=class_name, school_name=school_name, game_name=game_name)
        data.save()
        return redirect('students')

    return render(request, 'register.html')
