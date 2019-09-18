from django import template

register = template.Library()


@register.filter
def bool_filter(value):
    if value:
        return 'Есть'
    else:
        return 'Нет'
