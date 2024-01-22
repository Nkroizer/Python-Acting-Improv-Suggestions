from acting_improv_suggestion_generator import generate_improv_suggestion, Actor

yourself = Actor("Nati", "He")
players = ["Manny", "David", "Self"]
print(generate_improv_suggestion(yourself, players))
