from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from .models import Phone


def show_catalog(request):
    template = 'catalog.html'

    sort = request.GET.get('sort')

    if sort == 'name':
        phones = Phone.objects.order_by('name')
    elif sort == 'min_price':
        phones = Phone.objects.order_by('price')
    elif sort == 'max_price':
        phones = Phone.objects.order_by('-price')
    else:
        phones = Phone.objects.all()

    context = {
        'phones': phones
    }

    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'

    try:
        phone = Phone.objects.get(slug=slug)

    except ObjectDoesNotExist:
        phone = None

    context = {
        'phone': phone
    }

    return render(request, template, context)
