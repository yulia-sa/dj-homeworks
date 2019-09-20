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
        date = ''

    books = Book.objects.filter(pub_date=date)

    print(books)
    

    context = {
        'books': books
    }

    return render(request, template, context)
