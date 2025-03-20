from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, reverse
import os


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.now().time().strftime("%H:%M:%S")
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    directory = './1.1-first-project/first_project'
    files_list = [item for item in os.listdir(directory)]
    files_text = '\n'.join(files_list)
    return HttpResponse(files_text, content_type='text/plain')
