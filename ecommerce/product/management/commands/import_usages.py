import csv
from django.core.management.base import BaseCommand
from ...models import Category, Usage

class Command(BaseCommand):
    help = 'Import Categories from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csvs/usages.csv', type=str, help='The path to the CSV file to import')

    def handle(self, *args, **kwargs):
        csv_filepath = kwargs['csvs/usages.csv']
        
        try:
            with open(csv_filepath, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)

                if reader.fieldnames is None:
                    raise ValueError("CSV file is empty or missing header row.")
                
                count = 0

                for row in reader:
                    try:
                        usages_name = row['Name']
                        usages, created = Usage.objects.get_or_create(name=usages_name)
                        if created:
                            count += 1
                    except Exception as e:
                        self.stderr.write(self.style.ERROR(f'Error processing row: {e}'))

                    

                self.stdout.write(self.style.SUCCESS(f'Successfully imported {count} items.'))
        except FileNotFoundError:
            self.stderr.write(self.style.ERROR(f'File "{csv_filepath}" not found.'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Error: {e}'))
