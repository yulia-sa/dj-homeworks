from datetime import datetime

from django.shortcuts import render

from books.models import Book


def books_view(request):
    template = 'books/books_list.html'

    books = Book.objects.all()

    context = {
        'books': books
    }

    return render(request, template, context)


def date_books_view(request, year, month, day):
    template = 'books/books_list.html'

    try:
        date = datetime(year=year, month=month, day=day).date()

    except (ValueError, TypeError):
        context = {
            'books': ''
        }

        return render(request, template, context)

    books = Book.objects.filter(pub_date=date)
 
    try:
        previous_pub_dates_dict = Book.objects.values('pub_date').order_by('pub_date').filter(pub_date__lt=date)
        previous_pub_date = previous_pub_dates_dict.reverse()[0]['pub_date']
    except IndexError:
        previous_pub_date = ''

    try:
        next_pub_dates_dict = Book.objects.values('pub_date').order_by('pub_date').filter(pub_date__gt=date)
        next_pub_date = next_pub_dates_dict[0]['pub_date']
    except IndexError:
        next_pub_date = ''

    context = {
        'books': books,
        'previous_pub_date': previous_pub_date,
        'next_pub_date': next_pub_date
    }

    return render(request, template, context)
