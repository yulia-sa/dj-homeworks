import csv

from django.core.management.base import BaseCommand
from phones.models import Phone

from main.settings import PHONES_CSV


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open(PHONES_CSV, 'r') as csvfile:

            phone_reader = csv.reader(csvfile, delimiter=';')
            # пропускаем заголовок
            next(phone_reader)

            for line in phone_reader:
                phone = Phone.objects.get_or_create(
                    id = line[0],
                    name = line[1],
                    image = line[2],
                    price = line[3],
                    release_date = line[4],
                    lte_exists = line[5],
                )


if __name__ == '__main__':
    Command.handle()
