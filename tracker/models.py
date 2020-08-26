from django.db import models

ALL_CLASSES = []


def register_class(cls):
    ALL_CLASSES.append(cls)
    return cls


@register_class
class PlayerCharacter(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return f"PlayerCharacter({self.name})"


@register_class
class Prompt(models.Model):
    text = models.TextField(default="")
    number = models.IntegerField()
    subprompt_number = models.IntegerField(default=1)

    def __str__(self):
        return f"Prompt{self.number}.{self.subprompt_number}"


@register_class
class Event(models.Model):
    prompt = models.ForeignKey(Prompt, on_delete=models.CASCADE)
    timeline_index = models.IntegerField(default=0)

    def __str__(self):
        return f"Event #{self.timeline_index}"


@register_class
class Resource(models.Model):
    text = models.CharField(max_length=256)
    stationary = models.BooleanField(default=False)
    gainedBy = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='+')
    lostBy = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='+')

    def __str__(self):
        return f"Resource: {self.text}"


@register_class
class Diary(models.Model):
    description = models.CharField(max_length=256)
    gainedBy = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='+')
    lostBy = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='+')

    def __str__(self):
        return f"Diary: {self.description}"


@register_class
class Memory(models.Model):
    theme = models.CharField(max_length=256)
    gainedBy = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='+')
    lostBy = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='+')
    diary = models.ForeignKey(Diary, on_delete=models.CASCADE, related_name='+')

    def __str__(self):
        return f"Memory: {self.text}"


@register_class
class Experience(models.Model):
    summary = models.CharField(max_length=256)
    text = models.TextField(default="")
    gainedBy = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='+')
    memory = models.ForeignKey(Memory, on_delete=models.CASCADE)

    def __str__(self):
        return f"Experience: {self.summary}"


@register_class
class Character(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(default="")
    gainedBy = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='+')
    lostBy = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='+')
    immortal = models.BooleanField(default=False)

    def __str__(self):
        return f"Character: {self.name}"


@register_class
class Skill(models.Model):
    text = models.CharField(max_length=256)
    gainedBy = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='+')
    checkedBy = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='+')
    lostBy = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='+')


@register_class
class Mark(models.Model):
    text = models.CharField(max_length=256)
    gainedBy = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='+')
    lostBy = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='+')
