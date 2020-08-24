from django.db import models


# TODO: add __str__ to each model for better command-lining

class PlayerCharacter(models.Model):
    name = models.CharField(max_length=256)


class Prompt(models.Model):
    text = models.CharField(max_length=256)
    number = models.IntegerField()
    subprompt = models.IntegerField(default=1)


class Event(models.Model):
    prompt = models.ForeignKey(Prompt, on_delete=models.CASCADE)
    previous = models.ForeignKey('Event', on_delete=models.CASCADE)


class Experience(models.Model):
    text = models.CharField(max_length=256)
    gainedBy = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='+')


class Memory(models.Model):
    text = models.CharField(max_length=256)
    experiences = models.ManyToManyField(Experience)
    gainedBy = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='+')
    lostBy = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='+')


class Diary(models.Model):
    text = models.CharField(max_length=256)
    memories = models.ManyToManyField(Memory)
    gainedBy = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='+')
    lostBy = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='+')


class Character(models.Model):
    text = models.CharField(max_length=256)
    gainedBy = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='+')
    lostBy = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='+')


class Resource(models.Model):
    text = models.CharField(max_length=256)
    stationary = models.BooleanField(default=False)
    gainedBy = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='+')
    lostBy = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='+')


class Skill(models.Model):
    text = models.CharField(max_length=256)
    gainedBy = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='+')
    checkedBy = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='+')
    lostBy = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='+')


class Mark(models.Model):
    text = models.CharField(max_length=256)
    gainedBy = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='+')
    lostBy = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='+')
