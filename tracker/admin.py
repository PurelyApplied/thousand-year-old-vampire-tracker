from django.contrib import admin

# from .models import ALL_CLASSES
#
# for c in ALL_CLASSES:
#     admin.site.register(c)
#

from django.contrib import admin

from .models import *


class ResourceInline(admin.TabularInline):
    model = Resource


class DiaryInline(admin.TabularInline):
    model = Diary


class MemoryInline(admin.TabularInline):
    model = Memory


class ExperienceInline(admin.TabularInline):
    model = Experience


class CharacterInline(admin.TabularInline):
    model = Character


class SkillInline(admin.TabularInline):
    model = Skill


class MarkInline(admin.TabularInline):
    model = Mark


class PromptInline(admin.TabularInline):
    model = Prompt


class EventAdmin(admin.ModelAdmin):
    inlines = [ResourceInline]


admin.site.register(Event, EventAdmin)
