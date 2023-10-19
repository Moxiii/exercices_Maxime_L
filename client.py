import requests


def search():
    search_options = ["artistId", "artistName", "tracks"]
    print("Choisissez le type de recherche :")
    for i, option in enumerate(search_options, start=1):
        print(f"{i}. {option}")
    choice = input("Entrez le numéro de l'option : ")
    try:
        choice = int(choice)
        if 1 <= choice <= len(search_options):
            search_type = search_options[choice - 1]
            search_input = input("Entrez la valeur de recherche : ")
            url = ""
            if search_type == "artistId":
                url = f"http://127.0.0.1:8000/artist/{search_input}"
            elif search_type == "artistName":
                url = f"http://127.0.0.1:8000/artist/search/{search_input}?name={search_input}"
            elif search_type == "tracks":
                url = f"http://127.0.0.1:8000/tracks/{search_input}"
            else:
                print("Type de recherche non valide.")
                return
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                print(data)
            else:
                print(f"Erreur {response.status_code}: {response.reason}")
        else:
            print("Choix invalide.")
    except ValueError:
        print("Veuillez entrer un numéro.")

go = True 
while go == True:
    choice = int(input("\nMenu Principal:\n\t[1] Recherche.\n\t[2] Quitter\n\t"))
    if (choice == 1) :
        search()
    else:
        go = False
    