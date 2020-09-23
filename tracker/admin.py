from django.contrib import admin
from django.contrib.contenttypes import admin as cta


from .models import *


class EffectInline(cta.GenericTabularInline):
    model = GameEffect
    extra = 0


class EventAdmin(admin.ModelAdmin):
    inlines = [
        EffectInline,
    ]
    pass


admin.site.register(Event, EventAdmin)
#
# admin.site.register(Event)

for c in ALL_CLASSES:
    admin.site.register(c)

