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
  


    elif choix == 2:
        to_delete = input("Entrez l'élément à retirer : ")

        with open("liste.json", "r") as f:
            contenu = json.load(f)
            if to_delete.lower() in contenu:
                contenu.remove(to_delete)
                print("votre élément à été supprimé avec succès")
            else:
                print("votre élément n'existe pas")

        with open("liste.json", "w") as f:
            json.dump(contenu, f)




    elif choix == 3:
        with open("liste.json", "r") as f:
            contenu = json.load(f)
            
            if not contenu:
                print("Votre liste est vide.")
            else:
                for index, element in enumerate(contenu):
                    print(f"{index + 1}. {element}")


    
    elif choix == 4:
        confirm = int(input("Etes-vous sûr de vider la liste ? 1. Oui / 2. Non : "))
        if confirm == 1:
            with open("liste.json", "r") as f:
                contenu = json.load(f)

                if not contenu:
                    print("Votre liste est déjà vide.")
                else:    
                    contenu.clear()
            
            with open("liste.json", "w") as f:
                json.dump(contenu, f)
        
    elif choix == 5:
        print("Vous avez quitté le programme")
        break

    else:
        print("Veuillez entrer un choix entre 1 et 5.")
            
        


    
