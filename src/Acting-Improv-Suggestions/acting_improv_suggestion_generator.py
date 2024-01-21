import random
import improv_data


def generate_improv_suggestion():
    charAction = (
        "Nati is "
        + random.choice(improv_data.emotionDescriptors)
        + " "
        + random.choice(improv_data.emotions)
    )
    charAction += " That " + random.choice(improv_data.players)
    charAction += " " + random.choice(improv_data.conjunctions)
    charAction += " " + random.choice(improv_data.verbs)
    charAction += " A " + random.choice(improv_data.adjectives)
    selectedNoun = random.choice(improv_data.nouns)
    charAction += " " + selectedNoun
    if "Demon" in selectedNoun:
        charAction += " (" + random.choice(improv_data.demons) + ")"
    return charAction
