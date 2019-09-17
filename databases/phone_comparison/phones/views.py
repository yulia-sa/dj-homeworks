from django.shortcuts import render

from .models import Phone, AppleFeatures, GinzzuFeatures, MotorolaFeatures


def show_catalog(request):
    template = 'catalog.html'

    fields = [f.verbose_name for f in Phone._meta.get_fields()][1:]  # не выводим название поля ID
    phones = Phone.objects.all()

    apple_features = AppleFeatures.objects.all()
    ginzzu_features = GinzzuFeatures.objects.all()
    motorola_features = MotorolaFeatures.objects.all()

    context = {
        'fields': fields,
        'phones': phones,
        'apple_features': apple_features,
        'ginzzu_features': ginzzu_features,
        'motorola_features': motorola_features,
    }

    return render(
        request,
        template,
        context
    )
