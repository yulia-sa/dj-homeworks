from django import template

register = template.Library()


@register.filter
def existence_filter(value):
    if value == True:
        return 'Есть'
    else:
        return '—'
