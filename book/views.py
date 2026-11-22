from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.utils import timezone
# Create your views here.

# Про datetime вот я помню, потом посмотрел, оказалось, что есть еще один вариант для самого django
def about_me(request):
    if request.method == 'GET':
        return HttpResponse(
            '<h1>Меня зовут Давлатбеков Байэль</h1> ' \
            '<h3>Это мой учебный проект. Она будет представлять псевдо-библиотеку</h3>')

def writers(request):
    if request.method == 'GET':
        return HttpResponse('Писатели, которые мне нравятся давно: <br>' \
        'Эрнест Хеммингуэй, Ричард Мэтисон, Брэм Стокер, Фрэнк Герберт<br>' \
        '<br>' \
        'Авторы, книги которых мне понравились из последнего чтива: <br>' \
        'Нил Гейман, Марк Аврелий, Данте Алигьери, Адам Грант, Антонина Гилева')

def dateTime(request):
    if request.method == 'GET':
        # current_time = datetime.now().strftime('')
        now = timezone.localtime(timezone.now()).strftime('%d.%m.%Y %H:%M:%S')
        return HttpResponse(now)