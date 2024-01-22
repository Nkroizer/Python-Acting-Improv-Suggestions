import random
from typing import List
import improv_data


def generate_improv_suggestion(your_name: str, players: List[str]) -> str:
    charAction = (
        your_name
        + " is "
        + random.choice(improv_data.emotionDescriptors)
        + " "
        + random.choice(improv_data.emotions)
    )
    charAction += " That " + random.choice(players)
    charAction += " " + random.choice(improv_data.conjunctions)
    charAction += " " + random.choice(improv_data.verbs)
    charAction += " A " + random.choice(improv_data.adjectives)
    selectedNoun = random.choice(improv_data.nouns)
    charAction += " " + selectedNoun
    if "Demon" in selectedNoun:
        charAction += " (" + random.choice(improv_data.demons) + ")"
    return charAction
