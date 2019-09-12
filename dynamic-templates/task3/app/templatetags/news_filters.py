from datetime import datetime
from django import template


register = template.Library()


@register.filter
def format_date(value):

    now = datetime.now().timestamp()
    time_delta = now - value

    # Если пост был меньше 10 минут назад, пишет "только что"
    if time_delta < 600:
        return 'Только что'

    # Если пост был меньше 1 часа назад, пишет "X минут назад"
    elif 600 <= time_delta < 3600:
        return '{} минут назад'.format(int(time_delta / 60))

    # Если пост был меньше 24 часов назад, пишет "X часов назад"
    elif 3600 <= time_delta < 86400:
        return '{} часов назад'.format(int(time_delta / 3600))

    # Если пост был больше 24 часов назад, выводит дату в формате "Год-месяц-число"
    elif time_delta >= 86400:
        return datetime.fromtimestamp(value).strftime('%Y-%m-%d')

    else:
        return 'Неизвестна'


@register.filter
def score_mapping(score='Неизвестен'):

    # Рейтинг меньше -5, пишет "все плохо"
    try:
        if score < -5:
            return 'Всё плохо'

        # Рейтинг от -5 до 5 – "нейтрально"
        elif -5 <= score < 5:
            return 'Нейтрально'

        # Рейтинг больше 5 – "хорошо"
        elif score >= 5:
            return 'Хорошо'

    except (TypeError, ValueError):
        return 'Неизвестен'


@register.filter
def format_num_comments(num_comments):

    # Если комментариев 0, пишется "Оставьте комментарий"
    try:
        if num_comments == 0:
            return 'Оставьте комментарий'

        # От 0 до 50, пишем число комментариев
        elif 0 < num_comments <= 50:
            return num_comments

        # Больше 50, пишем "50+"
        if num_comments > 50:
            return '50+'

    except (TypeError, ValueError):
        return num_comments


# format_selftext:
# Оставляет count первых и count последних слов, между ними должно быть троеточие. 
# count задается параметром фильтра. 
# Пример c count = 5: "Hi all sorry if this ... help or advice greatly appreciated."
# Знаки препинания остаются, обрезаются только слова.

@register.filter
def format_selftext(text, words_count):

    words = text.split()

    if len(words) <= words_count * 2:
        return text

    text_beginning = ' '.join(words[0:5])
    text_end = ' '.join(words[-5:])

    result = text_beginning + ' ... ' + text_end

    return result
