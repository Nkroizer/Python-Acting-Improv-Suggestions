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
    # Adjective
    adjective = random.choice(improv_data.adjectives)
    # The Incident
    incident = random.choice(improv_data.incidents)
    if incident == "Possession":
        # They are possessed by something, but by what?
        charAction += " is possessed by "
        PossessionType = random.choice(improv_data.PossessionTypes)
        if PossessionType == "Human":
            # They are possessed by a (living) human
            humanType = random.choice(improv_data.humanTypes)
            if humanType == "Worker":
                # The Human that posses them is a worker
                profession = random.choice(improv_data.professions)
                charAction += " a " + adjective + " " + profession
        elif PossessionType == "Animal":
            animalType = random.choice(improv_data.animalTypes)
            charAction += " a " + adjective + " " + animalType
        elif PossessionType == "Plant":
            plantType = random.choice(improv_data.plantTypes)
            if plantType == "Fruits":
                fruit = random.choice(improv_data.fruits)
                charAction += " a " + adjective + " " + fruit
            elif plantType == "Vegetables":
                vegetable = random.choice(improv_data.vegetables)
                charAction += " a " + adjective + " " + vegetable
            else:
                charAction += " a " + adjective + " " + plantType
    charAction += " " + incident
    selectedNoun = random.choice(improv_data.nouns)
    charAction += " " + selectedNoun
    if "Demon" in selectedNoun:
        charAction += " (" + random.choice(improv_data.demons) + ")"
    return charAction
