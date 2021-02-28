import json

def kind(dict):
    if dict["q"] is not None:
        if yes[0] in dict:
            return "Decision"
        else:
            return "Animal"


yes = ["ja", "Ja", "JA", "ja.", "Ja.", "JA."]
no = ["nein", "Nein", "NEIN", "nein.", "Nein.", "NEIN."]

start = "Kann es fliegen?\n"

Papagei = {"q": "Ist es ein Papagei?\n", "info": "Papagei"}

Hund = {"q": "Ist es ein Hund?\n", "info": "Hund"}

game = {"q": start, yes[0]: Papagei, no[0]: Hund}




# while answer != 0:

# if answer in yes:
#     answer = input("Ist es ein Papagei?\n")
#     if answer in yes:
#         print("Super, bis zum nächsten Mal!")
#         answer = 0
#     if answer in no:
#         animal1 = input("Wie heißt dein Tier?\n")

# Entscheidungsfragen und Tierfragen

# binärer Baum mit E und  T
# E: bewege dich zu E[answer]
# T: answer in yes: Ende
# T: answer in no: fasse Tier T' auf, fasse Frage E' auf, wandele altes Tier  T in E'
# um und setze an E'[yes] T' und an E'[no] T

no_statement = "Vielen Dank, das werde ich mir merken.\n"

yes_statement = "Super, Bravo an mich selbst! Bis dann.\n"

with open("new_animals.json", "r") as treefile:
   game = json.load(treefile)

node = game

while True:
    answer = input(node["q"])
    if answer == "STOP":
        continue
    if answer not in yes and answer not in no:
        continue
    if kind(node) == "Decision":
        node = node[answer] # springe zur Antwort
    elif kind(node) == "Animal":
        if answer in no:
            yes_node_animal = input("Wie heißt dein Tier?\n") # Tier des Benutzers
            if answer == "STOP":
                continue
            new_node_question = input("Welche Frage ist besser für das Tier?\n") # neue Frage
            no_node_animal = node["info"] # altes Tier im Knoten
            node["q"] = new_node_question # oberen Knoten zu Frage umwandeln
            node[yes[0]] = {"q": "Ist es ein(e) " + yes_node_animal + "?\n", "info": yes_node_animal} # neues Tier
            node[no[0]] = {"q": "Ist es ein(e) " + no_node_animal + "?\n", "info": no_node_animal} # altes Tier
            answer = input("Bestätigen:\n")
            if answer == "STOP":
                continue
            print(no_statement)

            with open("new_animals.json", "w") as treefile:
                json.dump(game, treefile)
            node = game


        elif answer in yes:
            print(yes_statement)
            break

