from django.contrib import admin

from account.models import Penerima, Penyedia

# Register your models here.
admin.site.register(Penyedia)
admin.site.register(Penerima)
