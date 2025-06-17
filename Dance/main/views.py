from django.shortcuts import render, redirect
from .models import Style, Teacher, Price, UserProfile
from django.contrib import messages

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
    save = {}  # Инициализируем словарь в начале функции
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        lastname = request.POST.get('lastname', '').strip()
        surname = request.POST.get('surname', '').strip()
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')

        save.update({
            'username': username,
            'lastname': lastname,
            'surname': surname,
            'email': email,
            'phone': phone,
        })

        if len(username) < 2 or len(username) > 32:
            messages.error(request, 'Имя пользователя от 2 до 32 символов')
        elif len(lastname) < 2 or len(lastname) > 32:
            messages.error(request, 'Фамилия от 2 до 32 символов')
        elif len(surname) < 2 or len(surname) > 32:
            messages.error(request, 'Отчество от 2 до 32 символов')
        elif UserProfile.objects.filter(username=username).exists():
            messages.error(request, 'Пользователь с таким именем уже существует')
        else:
            UserProfile.objects.create(
                username=username,
                last_name=lastname,
                surname=surname,
                phone=phone
            )
            return redirect('home')

    return render(request, 'main/registration.html', save)

def rules(request):
    return render(request, 'main/rules.html')






