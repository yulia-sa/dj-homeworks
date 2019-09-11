import csv

from django.shortcuts import render

from app.settings import INFLATION_RUSSIA_CSV


def inflation_view(request):
    template_name = 'inflation.html'

    # чтение csv-файла и заполнение контекста
    with open(INFLATION_RUSSIA_CSV, newline='') as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        headings = next(reader)
        rows = list(reader)

    context = {
        'headings': headings,
        'rows': rows,
    }

    return render(request, template_name,
                  context)
