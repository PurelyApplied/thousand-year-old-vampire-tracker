from django.contrib import admin

from .models import ALL_CLASSES

for c in ALL_CLASSES:
    admin.site.register(c)

