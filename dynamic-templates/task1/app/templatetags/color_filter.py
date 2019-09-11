from django import template

register = template.Library()


@register.filter
def color_filter(inflation):
    try:
        inflation_value = float(inflation)

        if inflation_value < 0:
            return 'green'
        elif 1.0 < inflation_value <= 2.0:
            return '#FFCBCB'
        elif 2.0 < inflation_value <= 5.0:
            return '#FF6565'
        elif inflation_value > 5.0:
            return '#FF0000'
        else:
            return 'transparent'

    except ValueError:
        return 'transparent'
