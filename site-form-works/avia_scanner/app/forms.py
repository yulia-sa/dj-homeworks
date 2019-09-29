from django import forms

from .widgets import AjaxInputWidget
from .models import City


class SearchTicket(forms.Form):
    city_from = forms.CharField(
        widget=AjaxInputWidget(
            'api/city_ajax', 
            attrs={
            'class': 'inline right-margin'
            }
        ), 
        max_length=50, 
        label='Город отправления'
    )
    city_to = forms.ChoiceField( 
        label='Город назначения', 
        choices=[(choice.pk, choice) for choice in City.objects.all().order_by('name')], 
        widget=forms.Select(
            attrs={
                'class': 'inline right-margin'
            }
        ),
    )
    date = forms.DateField(
        label='Дата',
        widget=forms.SelectDateWidget
    )
