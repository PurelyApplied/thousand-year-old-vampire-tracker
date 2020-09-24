import itertools

from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models

REGISTERED_CLASSES = []


def register_class(cls):
    REGISTERED_CLASSES.append(cls)
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
        return f"PlayerCharacter({self.name}, {self.game})"


@register_class
class Prompt(models.Model):
    number = models.IntegerField()
    subprompt_number = models.IntegerField(default=1)
    text = models.TextField(default="")

    def __str__(self):
        return f"Prompt({self.number}, {self.subprompt_number})"


class Event(models.Model):
    short_title = models.TextField(default="")
    player = models.ForeignKey(PlayerCharacter, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    prompt = models.ForeignKey(Prompt, on_delete=models.CASCADE)

    def __str__(self):
        if self.short_title:
            return f"Event({self.short_title})"
        return f"Event(id={self.id}, {self.player}, {self.game})"


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
        return f"Effect({self.kind.capitalize()}, {self.noun})"


@register_class
class Memory(models.Model):
    rqn = 'memory'

    effects = GenericRelation(GameEffect, related_query_name=rqn)

    theme = models.CharField(max_length=256)

    def __str__(self):
        return f"Memory({self.theme})"

    def rqn_kw(self):
        return {self.rqn: self}


@register_class
class Experience(models.Model):
    summary = models.CharField(max_length=256)
    text = models.TextField(default="")

    memory = models.ForeignKey(Memory, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return f"Experience({self.summary})"


@register_class
class Character(models.Model):
    rqn = 'character'

    effects = GenericRelation(GameEffect, related_query_name=rqn)

    name = models.CharField(max_length=256)
    description = models.TextField(default="")
    immortal = models.BooleanField(default=False)

    def __str__(self):
        return f"Character({self.name})"

    def rqn_kw(self):
        return {self.rqn: self}


@register_class
class Diary(models.Model):
    rqn = 'diary'

    effects = GenericRelation(GameEffect, related_query_name=rqn)

    description = models.CharField(max_length=256)

    def __str__(self):
        return f"Diary({self.description})"

    def rqn_kw(self):
        return {self.rqn: self}


@register_class
class Resource(models.Model):
    rqn = 'resource'

    effects = GenericRelation(GameEffect, related_query_name=rqn)
    text = models.CharField(max_length=256)

    stationary = models.BooleanField(default=False)

    def __str__(self):
        return f"Resource({self.text})"

    def rqn_kw(self):
        return {self.rqn: self}


@register_class
class Skill(models.Model):
    rqn = 'skill'

    effects = GenericRelation(GameEffect, related_query_name=rqn)
    text = models.CharField(max_length=256)

    def __str__(self):
        return f"Skill({self.text})"

    def rqn_kw(self):
        return {self.rqn: self}


@register_class
class Mark(models.Model):
    rqn = 'mark'

    effects = GenericRelation(GameEffect, related_query_name=rqn)
    text = models.CharField(max_length=256)

    def __str__(self):
        return f"Mark({self.text})"

    def rqn_kw(self):
        return {self.rqn: self}


def current_character_sheet(game: Game, player: PlayerCharacter):
    events = Event.objects.filter(game=game, player=player)
    effects = GameEffect.objects.filter(event__in=events)
    nouns = set(e.noun for e in effects)
    states = {
        n: GameEffect.objects.filter(**n.rqn_kw()).order_by("-id")[0].kind
        for n in nouns
    }

    return states
