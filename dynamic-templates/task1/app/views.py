import csv

from django.shortcuts import render

from app.settings import INFLATION_RUSSIA_CSV

def inflation_view(request):
    template_name = 'inflation.html'

    # чтение csv-файла и заполнение контекста
    with open(INFLATION_RUSSIA_CSV, newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        csv_headings = next(csv_reader)
        reader_list = list(csv_reader)


    context = {
        'headings': csv_headings,
        'rows': reader_list,
    }

    return render(request, template_name,
                  context)
