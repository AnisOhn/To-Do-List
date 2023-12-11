import json



print("Bienvenue dans la ToDoList")

choix = 0

while choix != 5:
    print("----------------------------------------------------------")
    print("Choisissez parmi les 5 options suivantes : ")
    print("1: Ajouter un élément à la liste.")
    print("2: Retirer un élément de la liste.")
    print("3: Afficher la liste.")
    print("4: Vider la liste.")
    print("5: Quitter.")

    choix = int(input("Tapez votre choix : "))


    if choix == 1:
        new_task = input("Entrez votre élément : ")

        with open("liste.json", "r") as f:
            contenu = json.load(f)
        
        contenu.append(new_task)

        with open("liste.json", "w") as f:
            json.dump(contenu, f)
  


    if choix == 3:
        with open("liste.json", "r") as f:
            contenu = json.load(f)
            for index, element in enumerate(contenu):
                print(f"{index + 1}. {element}")


    
