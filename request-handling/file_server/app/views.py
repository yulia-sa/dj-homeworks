import os
from datetime import datetime

from django.shortcuts import render
from app.settings import FILES_PATH


def file_list(request, date=None):
    template_name = 'index.html'
    
    files = os.listdir(FILES_PATH)
    files_with_info = []

    try:
        parsed_date = datetime.strptime(date, '%Y-%m-%d').date()
    except (ValueError, TypeError):
        parsed_date = ''

    for file_name in files:
        file_path = os.path.join(FILES_PATH, file_name)

        ctime = datetime.fromtimestamp(os.stat(file_path).st_ctime)
        mtime = datetime.fromtimestamp(os.stat(file_path).st_mtime)

        if date and parsed_date != ctime.date():
            continue

        file_info = {
            'name': file_name,
            'ctime': ctime,
            'mtime': mtime
        }
        files_with_info.append(file_info)

    context = {
        'files': files_with_info,
        'date': parsed_date if date else ''  # Этот параметр необязательный
    }

    return render(request, template_name, context)


def file_content(request, name):
    template_name = 'file_content.html'

    files = os.listdir(FILES_PATH)

    for file_name in files:
        if file_name == name:
            file_path = os.path.join(FILES_PATH, file_name)
            with open(file_path, 'r') as f:
                content = f.read()

    return render(
        request,
        template_name,
        context={'file_name': name, 'file_content': content}
    )
