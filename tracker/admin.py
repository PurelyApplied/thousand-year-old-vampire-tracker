from django.contrib import admin

from .models import *


class ResourceEffectInline(admin.TabularInline):
    model = ResourceEffect
    extra = 0


class SkillEffectInline(admin.TabularInline):
    model = SkillEffect
    extra = 0


class CharacterEffectInline(admin.TabularInline):
    model = CharacterEffect
    extra = 0


class MemoryEffectInline(admin.TabularInline):
    model = MemoryEffect
    extra = 0


class DiaryEffectInline(admin.TabularInline):
    model = DiaryEffect
    extra = 0


class MarkEffectInline(admin.TabularInline):
    model = MarkEffect
    extra = 0


class EventAdmin(admin.ModelAdmin):
    inlines = [
        ResourceEffectInline,
        SkillEffectInline,
        CharacterEffectInline,
        MemoryEffectInline,
        DiaryEffectInline,
        MarkEffectInline,
    ]
    pass


admin.site.register(Event, EventAdmin)
