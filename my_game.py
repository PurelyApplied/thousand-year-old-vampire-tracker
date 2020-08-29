from tracker.models import *


def get_or_create(cls, **kwargs):
    return cls.objects.get_or_create(**kwargs)[0]


def populate(do_save=False):
    base_prompts = (
        Prompt.objects.get_or_create(number=i, subprompt_number=sub, text=f"Placeholder text for prompt {i}.{sub}")[0]
        for i in range(1, 71) for sub in range(1, 4)
    )

    game = get_or_create(Game, name="Nicol's Flight")

    player = get_or_create(PlayerCharacter, name="Nicol Rhom", game=game)

    prompt_zero = get_or_create(Prompt, number=0, text="Character creation")

    new_game_event = get_or_create(Event, prompt=prompt_zero, player=player, game=game)

    m = get_or_create(Mark, text="You are always cold to the touch.  Your lips are blue.")
    get_or_create(MarkEffect, event=new_game_event, kind="gain", noun=m)

    merc = get_or_create(Skill, text="mercantile")
    get_or_create(SkillEffect, kind="gain", event=new_game_event, noun=merc)
    boating = get_or_create(Skill, text="boating")
    get_or_create(SkillEffect, kind="gain", event=new_game_event, noun=boating)
    sewing = get_or_create(Skill, text="sewing")
    get_or_create(SkillEffect, kind="gain", event=new_game_event, noun=sewing)

    money = get_or_create(Resource, text="a modest sum of money")
    get_or_create(ResourceEffect, kind="gain", event=new_game_event, noun=money)
    cloak = get_or_create(Resource, text="a fine cloak")
    get_or_create(ResourceEffect, kind="gain", event=new_game_event, noun=cloak)
    skiff = get_or_create(Resource, text="a skill at the river")
    get_or_create(ResourceEffect, kind="gain", event=new_game_event, noun=skiff)

    papa = get_or_create(Character, name="papa")
    get_or_create(CharacterEffect, kind="gain", event=new_game_event, noun=papa)
    anna = get_or_create(Character, name="Anna")
    get_or_create(CharacterEffect, kind="gain", event=new_game_event, noun=anna)
    calhun = get_or_create(Character, name="Calhun")
    get_or_create(CharacterEffect, kind="gain", event=new_game_event, noun=calhun)
    krampus = get_or_create(Character, name="Krampus")
    get_or_create(CharacterEffect, kind="gain", event=new_game_event, noun=krampus)

    memory_self = get_or_create(Memory, theme="self")
    get_or_create(MemoryEffect, kind="gain", event=new_game_event, noun=memory_self)
    memory_family = get_or_create(Memory, theme="family")
    get_or_create(MemoryEffect, kind="gain", event=new_game_event, noun=memory_family)
    memory_business = get_or_create(Memory, theme="business")
    get_or_create(MemoryEffect, kind="gain", event=new_game_event, noun=memory_business)
    memory_anna = get_or_create(Memory, theme="Anna")
    get_or_create(MemoryEffect, kind="gain", event=new_game_event, noun=memory_anna)
    memory_curse = get_or_create(Memory, theme="curse")
    get_or_create(MemoryEffect, kind="gain", event=new_game_event, noun=memory_curse)

    get_or_create(Experience,
                  summary="I am Nicol Rhom, son of Klaus, born and raised in Judenburg; I am happy as a fur "
                          "trader with my father in the mid 13th Century.",
                  memory=memory_self,
                  )
    get_or_create(Experience,
                  summary="Papa teaches me to drive a boat up and down the river to gather furs from trappers; "
                          "although he was upset that I capsized the boat and drenched us both, we laugh about "
                          "it now.",
                  memory=memory_family,
                  )
    get_or_create(Experience,
                  summary="Calhun drives a hard price for his skins and furs, but no one else brings us "
                          "otters; we have turned a tidy profit off him alone.",
                  memory=memory_business,
                  )
    get_or_create(Experience,
                  summary="Anna and I promised ourselves to each other beneath my cloak last summer; her "
                          "father and mine are at odds, though, and I worry we'll have to run away together.",
                  memory=memory_anna,
                  )
    get_or_create(Experience,
                  summary="Christmas Eve, Papa and I argued about my promise to Anna.  I slammed the door "
                          "behind me, cursing him and storming down to the river.  A stranger stood at the "
                          "shore.  We exchanged clipped words until he beat me with birch branches, "
                          "shoved me in a sack, and threw me into the frigid river, where I drowned but did "
                          "not die.",
                  memory=memory_curse,
                  )

    # Event 1
    prompt_1 = get_or_create(Prompt, number=4, subprompt_number=1,
                             text="""You are exposed and flee to a neighboring region.
Lose any stationary Resources. Check a Skill.
A mortal flees with you. What new name do you
adopt among these strangers?
""")

    event_1 = get_or_create(Event, prompt=prompt_1, player=player, game=game)
    get_or_create(Experience,
                  summary="Anna and I run away together, taking the skiff downriver, all the way to Leibnitz, "
                          "adopting the name Kühl; though I am terrified of what I am becoming, I am hopeful that "
                          "Anna will be a part of my life.",
                  memory=memory_anna,
                  )
    get_or_create(SkillEffect, kind="check", event=event_1, noun=boating)
    get_or_create(ResourceEffect, kind="lose", event=event_1, noun=skiff)

    # Event 2
    prompt_2 = get_or_create(Prompt, number=3, subprompt_number=1,
                             text="""A loved one discovers your condition and works
to help you. Create a Resource which represents
their assistance. Create a mortal Character if
none are available.
""")
    event_2 = get_or_create(Event, prompt=prompt_2, player=player, game=game)
    get_or_create(Experience,
                  summary="Once the dust of our escape has settled, Anna realizes the chill in my hands are not from "
                          "the weather, but does not hate me for being cursed; she is my solace in this troubled "
                          "storm.",
                  memory=memory_anna,
                  )

    gloves = get_or_create(Resource, text="fine silk gloves")
    get_or_create(ResourceEffect, kind="gain", event=event_2, noun=gloves)
