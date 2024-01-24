import random
from typing import List
import improv_data


class Actor:
    def __init__(self, name, pronoun):
        self.name = name
        self.pronoun = pronoun

    def __str__(self):
        return f"{self.name}({self.pronoun})"


def generate_improv_suggestion(main_actor: Actor, interactees: List[str]) -> str:
    random_person_to_interact_with = random.choice(interactees)
    charAction = (
        main_actor.name
        + " is "
        + random.choice(improv_data.emotionDescriptors)
        + " "
        + random.choice(improv_data.emotions)
    )
    if random_person_to_interact_with == "Self":
        charAction += " That " + main_actor.pronoun
    else:
        charAction += " That " + random_person_to_interact_with

    conjunction = random.choice(improv_data.conjunctions)
    charAction += " " + conjunction
    incident = random.choice(improv_data.incidents)
    charAction += " " + incident
    adjective = random.choice(improv_data.adjectives)
    charAction += " A " + adjective
    selectedNoun = random.choice(improv_data.nouns)
    charAction += " " + selectedNoun
    if "Demon" in selectedNoun:
        charAction += " (" + random.choice(improv_data.demons) + ")"
    return charAction
