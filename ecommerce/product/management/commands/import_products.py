import csv
from django.core.management.base import BaseCommand
from ...models import Category, SubCategory

class Command(BaseCommand):
    help = 'Import Categories from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csvs/categories.csv', type=str, help='The path to the CSV file to import')

    def handle(self, *args, **kwargs):
        csv_filepath = kwargs['csvs/categories.csv']
        
        try:
            with open(csv_filepath, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)

                if reader.fieldnames is None:
                    raise ValueError("CSV file is empty or missing header row.")
                
                count = 0

                for row in reader:
                    try:
                        sub_category = row['Name']
                        sub_category, created = SubCategory.objects.get_or_create(name=sub_category)
                        if created:
                            count += 1
                    except Exception as e:
                        self.stderr.write(self.style.ERROR(f'Error processing row: {e}'))

                    

                self.stdout.write(self.style.SUCCESS(f'Successfully imported {count} items.'))
        except FileNotFoundError:
            self.stderr.write(self.style.ERROR(f'File "{csv_filepath}" not found.'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Error: {e}'))
