from django.contrib import admin

# Register your models here.

from PythonDjango_.models import Topic
from PythonDjango_.models import Entry
admin.site.register(Topic)
admin.site.register(Entry)
