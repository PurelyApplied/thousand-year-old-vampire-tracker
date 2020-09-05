from django.contrib import admin

from .models import *


class EffectInline(admin.TabularInline):
    model = GameEffect
    extra = 0


class EventAdmin(admin.ModelAdmin):
    inlines = [
        EffectInline,
    ]
    pass


admin.site.register(Event, EventAdmin)

for c in ALL_CLASSES:
    admin.site.register(c)

