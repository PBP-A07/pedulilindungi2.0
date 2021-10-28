from django.contrib import admin

from main.models import Discussion, Questions

# Register your models here.
admin.site.register(Questions)
admin.site.register(Discussion)

