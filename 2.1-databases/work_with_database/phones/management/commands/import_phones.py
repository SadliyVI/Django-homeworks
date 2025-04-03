import csv
from datetime import datetime
from decimal import Decimal
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    help = 'Импортирует данные о телефонах из CSV-файла в базу данных'

    def add_arguments(self, parser):
        parser.add_argument('phones.csv', type=str, help='Путь к CSV-файлу')

    def handle(self, *args, **options):
        csv_file_path = options['phones.csv']
        try:
            with open(csv_file_path, 'r') as file:
                phones = list(csv.DictReader(file, delimiter=';'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'Файл "{csv_file_path}" не найден'))
            return
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Ошибка открытия файла: {e}'))
            return
        success_count = 0
        for phone in phones:
            try:
                Phone.objects.create(
                    id=int(phone['id']),
                    name=phone['name'].strip(),
                    image=phone['image'].strip(),
                    price=Decimal(phone['price']),
                    release_date=datetime.strptime(phone['release_date'], '%Y-%m-%d').date(),
                    lte_exists=phone['lte_exists'].strip().lower() == 'true'
                )
                success_count += 1
            except Exception as e:
                self.stdout.write(self.style.ERROR(
                    f'Ошибка в строке {phone}: {e}'
                ))
        self.stdout.write(
            self.style.SUCCESS(f'Успешно импортировано {success_count} из {len(phones)} записей')
        )
