from functools import reduce

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import *
from .models import Prompt


def detail(request, p_id):
    p = get_object_or_404(Prompt, pk=p_id)
    return render(request, 'prompts/detail.html', {'prompt': p})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def event(request, event_id):
    e = get_object_or_404(Prompt, pk=event_id)

    item = get_object_or_404(Event, pk=event_id)
    try:
        selected_choice = item.choice_set.get_or_create(pk=request.POST['choice'])
    except (KeyError, Event.DoesNotExist):
        # Redisplay the item voting form.
        return render(request, r'tracker/templates/prompts/index.html', {
            'item': item,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(item.id,)))


def index(request):
    prompts_list = Prompt.objects.order_by('number', 'subprompt_number')
    return render(request, 'prompts/index.html', {'prompts_list': prompts_list})


def new_event(request):
    e = Event()


def game(request, name):
    g = get_object_or_404(Game, name=name)
    pcs = list(PlayerCharacter.objects.filter(game=g))
    events = [
        e
        for p in pcs
        for e in list(Event.objects.filter(game=g, player=p))
    ]

    effects = {
        e: tuple(GameEffect.objects.filter(event=e))
        for e in events
    }


    return render(request, 'sheet/sheet.html', {
        'game': g,
        'player_characters': pcs,
        'events': events,
        'effects': tuple(effects.items()),
    })
