import csv

from django.shortcuts import render_to_response, redirect
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage

from app.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    with open(BUS_STATION_CSV, newline='', encoding="CP1251") as csvfile:
        reader = csv.DictReader(csvfile)
        reader_list = list(reader)

    paginator = Paginator(reader_list, 10)

    try:
        current_page = int(request.GET.get('page'))
        if current_page > paginator.num_pages:
            current_page = paginator.num_pages
    except (ValueError, TypeError):
        current_page = 1

    if paginator.page(current_page).has_previous():
        previous_page = paginator.page(current_page).previous_page_number()

    if paginator.page(current_page).has_next():
        next_page = paginator.page(current_page).next_page_number()

    context = {
        'bus_stations': paginator.page(current_page),
        'current_page': current_page,
        'prev_page_url': None if current_page <= 1 else '?page={}'.format(previous_page),
        'next_page_url': None if current_page >= paginator.num_pages else '?page={}'.format(next_page),
    }

    return render_to_response('index.html', context=context)
