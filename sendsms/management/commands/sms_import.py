from sendsms.models import *
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    # args = '<filename.csv filename2.csv ...>'
    # help = 'Import name/email/number (s) from CSV'
    # print("command {}".format(args))

    def add_arguments(self, parser):
        parser.add_argument('--file', type=str)

    def handle(self, *args, **options):
        import csv
        try:
            with open('filename.csv', newline='') as f:
                reader = csv.reader(f)
                for row in reader:
                    name = row[0]
                    email= row[1]
                    number=row[2]
                    print(name, number, email)
                    # save to database stripping quotes
                    SmsUser.objects.create(
                                        name = name,
                                        email= email,
                                        number = number,
                                    )
                    self.stdout.write('IMPORTED %s %s %s' % ( name, email, number))
        except Exception as e:
            print(e)
            self.stderr.write('ERROR IMPORTING %s' % (row))





Command