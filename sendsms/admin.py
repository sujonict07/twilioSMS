from django.contrib import admin

# Register your models here.
from .models import *


class SmsUserAdmin(admin.ModelAdmin):
    list_display  = ('name', 'number', 'email')
    search_fields = ['name', 'number', 'email']


admin.site.register(SmsUser, SmsUserAdmin)