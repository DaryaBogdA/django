from django.shortcuts import render
from .models import Style, Teacher, Price

def home(request):
    styles = Style.objects.all()
    teachers = Teacher.objects.all()
    prices = Price.objects.all()
    return render(request, 'main/home.html', {'styles':styles, 'teachers':teachers, 'prices':prices})

def kids_dance(request):
    return render(request, 'main/kids_dance.html')

def all_styles(request):
    return render(request, 'main/all_styles.html')

def rdc(request):
    return render(request, 'main/rdc.html')

def hiphop_7_9(request):
    return render(request, 'main/hiphop_7_9.html')

def junior_team(request):
    return render(request, 'main/junior_team.html')

def adult_team(request):
    return render(request, 'main/adult_team.html')

def registration(request):
    return render(request, 'main/registration.html')






