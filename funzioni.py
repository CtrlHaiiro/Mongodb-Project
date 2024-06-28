import os
import random
import time
from pymongo import MongoClient
import re

global collection


def start_client():
    # connects to mongodb database
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
        local = place["locale"]
        city = place["citta"]
        seats = place["posti"]

        print(f"\n{i + 1}- Città: {city}\n"
              f"Locale: {local}\n"
              f"Data: {', '.join(data)}, ore {time}\n"
              f"{seats['numero_posti']} posti disponibili\n"
              f"prezzo: {seats['prezzo']} €")


def purchase_page(event):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("purchase_page\n")
    print(event["nome"])
    seats = event["luogo"][0]["posti"]
    name_seats= seats["posti"]
    print(name_seats)

    num_biglietti = int(input("inserisci il numero biglietti da acquistare: "))

    choice = int(input(f"il prezzo totale per {num_biglietti} biglietti e': {seats['prezzo'] * num_biglietti} €\n"
                       f"- 1 per effettuare l'acquisto\n"
                       f"- 0 per tornare indietro\n"
                       f"inserisci scelta: "))
    if choice == 0:
        return purchase_page(event)

    elif choice == 1:
        print("da implementare\n")
        selected_seats = seats["posti"][:num_biglietti]
        new_list = [x for x in name_seats if x not in selected_seats]
        print(new_list)
        for seat in selected_seats:
            print(collection.find_one({"nome": event["nome"]}))
            collection.update_one({"nome": event["nome"]},
                                  {"$set": {f"luogo.0.posti.posti.{seat}": new_list}})
            collection.update_one({"nome": event["nome"]},
                                  {"$set": {f"luogo.0.posti.numero_posti": len(seats["posti"]) - num_biglietti}})
        print("acquisto effettuato con successo")
        time.sleep(2)
        return

    time.sleep(2)
    return


def show_avariable_concerts(concerts):
    print(f"concerti disponibili: \n"
          f"{len(concerts)} risultati trovati\n")
    for i, concert in enumerate(concerts):
        #print(f"{i + 1} - {concert["nome"]}  ")
        print( str(i+1) + " - " + concert["nome"] )
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
            purchase_page(results[choice])
        else:
            return search_concert()

    else:
        print("Nessun concerto trovato con questo nome.")
        time.sleep(2)

    time.sleep(1)


def search_artist():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("cerca per artista")
    query = {}
    artist = str(input("inserisci il nome del artista/band: ")).capitalize()
    regex_pattern = re.compile(f".*{re.escape(artist)}.*", re.IGNORECASE)

    query = {"artisti": {"$regex": regex_pattern}}
    results = list(collection.find(query))
    if results:
        choice = show_avariable_concerts(results)
        view_details(results[choice - 1])
        choice = int(input("\n0 - indietro\nseleziona una data: \n"))
        if choice != 0:
            purchase_page(results[choice])
        else:
            return show_avariable_concerts(results)
    else:
        print("Nessun artista trovato con questo nome.")
        time.sleep(2)

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
