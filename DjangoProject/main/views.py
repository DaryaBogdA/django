from django.shortcuts import render


def index(request):
    data = {
        'title': 'это уже тема 6',
        'array' : ['это', 'тема', '6'],
        'obj' : {
            'what': 'это',
            'this': 'тема',
            'tema': 6,
        }
    }

    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')

def phone(request):
    phones = {
        'title': "Наши контакты",
        'obj': {
            "Директор": "+37525465421",
            "Бухгалтер": "+37525465487",
            "Аренда": "+37525321421",
        }
    }
    return render(request, 'main/phone.html', phones)