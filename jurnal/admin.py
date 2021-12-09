from django.contrib import admin

from .models import Journal, Record

# Register your models here.
admin.site.register(Journal)
admin.site.register(Record)