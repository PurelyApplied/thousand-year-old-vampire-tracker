from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models

ALL_CLASSES = []


def register_class(cls):
    ALL_CLASSES.append(cls)
    return cls


@register_class
class Game(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return f"Game({self.name})"


@register_class
class PlayerCharacter(models.Model):
    name = models.CharField(max_length=256)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return f"PlayerCharacter({self.name})"


@register_class
class Prompt(models.Model):
    text = models.TextField(default="")
    number = models.IntegerField()
    subprompt_number = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.number}.{self.subprompt_number} Prompt"


class Event(models.Model):
    short_title = models.TextField(default="")
    prompt = models.ForeignKey(Prompt, on_delete=models.CASCADE)
    player = models.ForeignKey(PlayerCharacter, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        if self.short_title:
            return f"Game event: {self.short_title}"
        return f"Game event: {self.game} #{self.id}"


@register_class
class GameEffect(models.Model):
    class Kind(models.TextChoices):
        GAIN = "gain"
        LOSE = "lose"
        CHECK = "check"
        DIARY = "diary"

    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    kind = models.TextField(choices=Kind.choices)

    limit = (
            models.Q(app_label='tracker', model='character') |
            models.Q(app_label='tracker', model='diary') |
            models.Q(app_label='tracker', model='resource') |
            models.Q(app_label='tracker', model='skill') |
            models.Q(app_label='tracker', model='mark') |
            models.Q(app_label='tracker', model='memory')
    )

    content_type = models.ForeignKey(ContentType,
                                     limit_choices_to=limit, on_delete=models.CASCADE,
                                     default=None, blank=True, null=True)
    object_id = models.PositiveIntegerField(default=None, blank=True, null=True)
    noun = GenericForeignKey()

    def __str__(self):
        return f"Effect: {self.kind.capitalize()} -- {self.noun}"


@register_class
class Memory(models.Model):
    effects = GenericRelation(GameEffect, related_query_name='memory')

    theme = models.CharField(max_length=256)

    def __str__(self):
        return f"Memory: {self.theme}"


@register_class
class Experience(models.Model):
    summary = models.CharField(max_length=256)
    text = models.TextField(default="")
    memory = models.ForeignKey(Memory, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return f"Experience: {self.summary}"


@register_class
class Character(models.Model):
    effects = GenericRelation(GameEffect, related_query_name='character')

    name = models.CharField(max_length=256)
    description = models.TextField(default="")
    immortal = models.BooleanField(default=False)

    def __str__(self):
        return f"Character: {self.name}"


@register_class
class Diary(models.Model):
    effects = GenericRelation(GameEffect, related_query_name='diary')

    description = models.CharField(max_length=256)

    def __str__(self):
        return f"Diary: {self.description}"


@register_class
class Resource(models.Model):
    effects = GenericRelation(GameEffect, related_query_name='resource')

    text = models.CharField(max_length=256)
    stationary = models.BooleanField(default=False)

    def __str__(self):
        return f"Resource: {self.text}"


@register_class
class Skill(models.Model):
    effects = GenericRelation(GameEffect, related_query_name='skill')

    text = models.CharField(max_length=256)

    def __str__(self):
        return f"Skill: {self.text}"


@register_class
class Mark(models.Model):
    effects = GenericRelation(GameEffect, related_query_name='mark')

    text = models.CharField(max_length=256)

    def __str__(self):
        return f"Mark: {self.text}"
