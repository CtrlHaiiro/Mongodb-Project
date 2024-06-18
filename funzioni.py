import os
import time
from pymongo import MongoClient
import re

global collection


def start_client():
#connects do mongodb database
    try:
        global collection
        client = MongoClient("mongodb://localhost:27017/")
        db = client.get_database("Concerti")
        collection = db.get_collection("concerti")
        return collection
    except Exception:
        print(Exception)


def view_details(event):
    os.system('cls' if os.name == 'nt' else 'clear')
    name = event["nome"]
    artists = event["artisti"]
    places = event["luogo"]

    print(f"Nome: {name}\n"
          f"Artisti : {', '.join(artists)}")

    for i, place in enumerate(places):

        data = place["tempo"]["data"]
        time = place["tempo"]["ora"]
        locale = place["locale"]
        city = place["citta"]
        posti = place["posti"]
        posti_vip = posti["vip"]["numero_posti"]
        posti_premium = posti["premium"]["numero_posti"]
        posti_base = posti["base"]["numero_posti"]
        posti_totali = posti_vip + posti_base + posti_premium

        print(f"\n{i + 1}- Città: {city}\n"
              f"Locale: {locale}\n"
              f"Data: {', '.join(data)}, ore {time}\n"
              f"{posti_totali} posti disponibili")


def purchase_page(event):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("purchase_page\n")
    print(event["nome"])
    concert_info = event["luogo"][0]
    posti = concert_info["posti"]
    categorie_posti = ["vip", "premium", "base"]
    for i, category in enumerate(categorie_posti):
        print(f"{i+1}- posti {category}\n"
              f"{posti[category]["numero_posti"]} posti disponibili\n")
    choice = int(input(f"0- indietro\n"
                   f"inserisci una scelta: "))
    if choice == 0:
        return search_concert()
    num_biglietti = int(input("inserisci numero biglietti da acquistare: "))
    print("da implementare\n")
    time.sleep(2)
    return search_concert()





    time.sleep(2)
    return


def show_avariable_concerts(concerts):
    print(f"concerti disponibili: \n"
          f"{len(concerts)} risultati trovati\n")
    for i, concert in enumerate(concerts):
        print(
            f"{i + 1} - {concert["nome"]}  ")
    choice = int(input("\ninserisci il numero del concerto \n"
                       "per visualizzare i dettagli ( 0 per tornare indietro ) : "))
    if choice == 0:
        return search_concert()
    else:
        return choice


def search_concert():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("cerca per concerto")
    query = {}
    concert = str(input("inserisci il nome del concerto: ")).capitalize()
    regex_pattern = re.compile(f".*{re.escape(concert)}.*", re.IGNORECASE)

    query = {"nome": {"$regex": regex_pattern}}
    results = list(collection.find(query))
    if results:
        choice = show_avariable_concerts(results)
        view_details(results[choice - 1])
        choice = int(input("\n0 - indietro\nseleziona una data: \n"))
        if choice != 0:
            purchase_page(results[choice - 1])
        else: return search_concert()

    else:
        print("Nessun concerto trovato con questo nome.")
        time.sleep(2)

    time.sleep(1)


def search_artist():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("cerca per artista")
    time.sleep(1)


def search_by_date():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("cerca per intervallo di date")
    time.sleep(1)


def search_by_distance():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("ricerca per distanza")
    time.sleep(1)


def exit_program():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("uscita dal programma")
    time.sleep(1)
