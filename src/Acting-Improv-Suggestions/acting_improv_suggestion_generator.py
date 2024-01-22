import random
from typing import List
import improv_data


class Actor:
    def __init__(self, name, pronoun):
        self.name = name
        self.pronoun = pronoun

    def __str__(self):
        return f"{self.name}({self.pronoun})"


def generate_improv_suggestion(yourself: Actor, players: List[str]) -> str:
    random_person_to_interact_with = random.choice(players)
    charAction = (
        yourself.name
        + " is "
        + random.choice(improv_data.emotionDescriptors)
        + " "
        + random.choice(improv_data.emotions)
    )
    if random_person_to_interact_with == "Self":
        charAction += " That " + yourself.pronoun
    else:
        charAction += " That " + random_person_to_interact_with
    charAction += " " + random.choice(improv_data.conjunctions)
    charAction += " " + random.choice(improv_data.verbs)
    charAction += " A " + random.choice(improv_data.adjectives)
    selectedNoun = random.choice(improv_data.nouns)
    charAction += " " + selectedNoun
    if "Demon" in selectedNoun:
        charAction += " (" + random.choice(improv_data.demons) + ")"
    return charAction
