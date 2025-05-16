from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
import csv

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    csv_file_path = settings.BUS_STATION_CSV
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        bus_stations_list = [
            {
                'Name': row['Name'],
                'Street': row['Street'],
                'District': row['District']
            }
            for row in reader
        ]  # Преобразуем генератор в список с нужными полями
    # Получаем текущую страницу из параметров запроса, по умолчанию 1
    page_number = int(request.GET.get('page', 1))
    stations_per_page = 10  # Количество станций на странице
    # Создаем объект Paginator
    paginator = Paginator(bus_stations_list, stations_per_page)
    # Получаем нужную страницу
    bus_stations_on_page = paginator.get_page(page_number)
    context = {
        'bus_stations': bus_stations_on_page,
        'page': bus_stations_on_page,
    }
    return render(request, 'stations/index.html', context)
