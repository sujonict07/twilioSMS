from sendsms.models import *
from django.conf import settings
from optparse import make_option
from twilio.rest import Client
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    args = '<text> --everyone | <number number ...>'
    help = 'Sends SMS text to the specified number(s) (or everyone)'
    print(args)
    can_import_settings = True

    option_list = BaseCommand.stealth_options + (
        make_option('--everyone',
                    action='store_true',
                    dest='everyone',
                    default=False,
                    help='Send SMS to everyone'),
                )

    def add_arguments(self, parser):
        parser.add_argument('--file', type=str)


    def handle(self, *args, **options):
        i = 0
        print("args {}".format(args))
        # text = args[0][:140]
        text = "hello world"

        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)


        # if options['everyone']:
        #     send_to = SmsUser.objects.all()
        # else:
        #     send_to = args[1:]
        #
        # for number in send_to:
        #     i += 1
        number = '+8801625099076'
        try:
            _send_sms(client, text, number)
            self.stdout.write('%d SENT TO %s' % (i, number))
        except Exception as e:
            print(e.code, e)
            raise CommandError("SMS sent failed")



def _send_sms(client, text, number):
    """
        See https://github.com/twilio/twilio-python/pull/189
    """

    # quick hack to make it work with 
    # both QuerySet objects and lists
    if type(number) == SmsUser:
        number = number.number

    print(number)
    print(text)
    print(settings.TWILIO_NUMBER)

    message = client.messages.create(body=text, to=number, from_=settings.TWILIO_NUMBER)
    print(message.sid)  # To print sid

    # account_sid = 'AC8c9ea33ad7b1f6cbd083281770820d9e'
    # auth_token = 'c99236a214dc12e5414d3fe2887b4300'
    # client = Client(account_sid, auth_token)
    #
    # message = client.messages.create(
    #     from_='+18142564874',
    #     to='+8801625099076',
    #     body = 'text'
    # )
    #
    # print(message.sid)
