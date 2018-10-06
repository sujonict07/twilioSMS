from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Command to do......"

    def add_arguments(self, parser):
        parser.add_argument('msg', nargs='+', type=str)

    def handle(self, *args, **options):
        try:
            print("i Am here")
            print(options)
            msg = options['abc']
            print(msg)
        except Exception as e:
            CommandError(repr(e))
