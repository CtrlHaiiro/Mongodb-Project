import os
import time
from datetime import datetime
import re
global collection
import geojson
from pymongo import MongoClient, GEOSPHERE


def start_client():
    # connects to mongodb database
    try:
        global collection
        client = MongoClient("mongodb://localhost:27017/")
        db = client.get_database("Concerti")
        collection = db.get_collection("concerti")
        collection.create_index([("luogo.coordinates", GEOSPHERE)])

        return collection
    except Exception as e:
        print(f"Errore nella connessione a {e}")


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
    print("Acquisto biglietti\n")
    print(event["nome"])
    event_id = event["_id"]
    seats = event["luogo"][0]["posti"]
    if seats is None:
        print("nessun biglietto disponibile")
        time.sleep(2)
        return purchase_page(event)
    name_seats = seats["posti"]

    try:
        num_biglietti = int(input("inserisci il numero biglietti da acquistare: "))
    except ValueError:
        print("inserisci un numero valido")
        time.sleep(2)
        return purchase_page(event)

    choice = int(input(f"il prezzo totale per {num_biglietti} biglietti e': {seats['prezzo'] * num_biglietti} €\n"
                       f"- 1 per effettuare l'acquisto\n"
                       f"- 0 per tornare indietro\n"
                       f"inserisci scelta: "))
    if choice == 0:
        return purchase_page(event)

    elif choice == 1:
        if num_biglietti > len(name_seats):
            print("nessun biglietto disponibile")
            time.sleep(2)
            return purchase_page(event)
        selected_seats = name_seats[:num_biglietti]
        new_list = [x for x in name_seats if x not in selected_seats]
        collection.update_one({"_id": event_id},
                          {"$set": {f"luogo.0.posti.posti": new_list}})

    # Aggiorna il numero di posti rimanenti per l'evento trovato
        collection.update_one({"_id": event_id},
                          {"$set": {f"luogo.0.posti.numero_posti": int(len(seats["posti"]) - num_biglietti)}})

        print(f"acquisto effettuato con successo\n"
              f"I posti acquistati sono: {[seat for seat in selected_seats]}")
    else:
        print("scelta non valida")
        return purchase_page(event)

    time.sleep(2)
    return


def show_avariable_concerts(concerts):
    print(f"concerti disponibili: \n"
          f"{len(concerts)} risultati trovati\n")
    for i, concert in enumerate(concerts):
        print( str(i+1) + " - " + concert["nome"] )
    try:
        choice = int(input("\ninserisci il numero del concerto \n"
                       "per visualizzare i dettagli ( 0 per tornare indietro ) : "))
        if choice == 0:
            return search_concert()
        else:
            return choice

    except ValueError:
        print("inserisci un numero valido")
        time.sleep(2)
        return show_avariable_concerts(concerts)


def search_concert():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("cerca per concerto")
    concert = str(input("inserisci il nome del concerto: ")).capitalize()
    regex_pattern = re.compile(f".*{re.escape(concert)}.*", re.IGNORECASE)

    query = {"nome": {"$regex": regex_pattern}}
    results = list(collection.find(query))
    if results:
        choice = show_avariable_concerts(results)
        view_details(results[choice - 1])
        date_choice = int(input("\n0 - indietro\nseleziona una data: \n"))
        if date_choice != 0:
            purchase_page(results[choice-1])
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
            return search_artist()
    else:
        print("Nessun artista trovato con questo nome.")
        time.sleep(2)

    time.sleep(1)


def search_by_date():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Cerca per data")
    while True:
        try:
            data1 = input("Inserisci la prima data per trovare il concerto (Anno-Mese-Giorno): ")
            data2 = input("Inserisci la seconda data per trovare il concerto (Anno-Mese-Giorno): ")
            date1 = datetime.strptime(data1, "%Y-%m-%d")
            date2 = datetime.strptime(data2, "%Y-%m-%d")
            break
        except ValueError:
            print("Errore: formato data non valido. Riprova!")

    date1_str = date1.strftime("%Y-%m-%d")
    date2_str = date2.strftime("%Y-%m-%d")

    query = {"luogo.tempo.data": {"$gte": date1_str, "$lte": date2_str}}
    results = list(collection.find(query))

    if results:
        choice = show_avariable_concerts(results)
        view_details(results[choice - 1])

        date_choice = int(input("\n0 - indietro\nseleziona una data: \n"))
        if date_choice != 0:
            purchase_page(results[choice-1])
        else:
            return search_concert()

    else:
        print("Nessun concerto trovato in questo intervallo di date.")
        while True:
            try:
                choice = int(input("\n0 - Indietro\n1 - Riprova con altre date\nSeleziona una opzione: "))
                if choice == 0:
                    time.sleep(1)
                    return
                elif choice == 1:
                    return search_by_date()
                else:
                    print("Scelta non valida. Riprova.")
            except ValueError:
                print("Errore: inserisci un numero valido.")


def search_by_distance():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("cerca per distanza")

    try:
        user_lat = float(input("Inserisci la tua latitudine: "))
        user_lon = float(input("Inserisci la tua longitudine: "))
        max_distance = float(7000)  # Distanza massima in metri

        if not (-90 <= user_lat <= 90):
            raise ValueError("Latitudine fuori dai limiti validi (-90 a 90).")
        if not (-180 <= user_lon <= 180):
            raise ValueError("Longitudine fuori dai limiti validi (-180 a 180).")
    except ValueError as e:
        print(f"Errore: {e}")
        time.sleep(2)
        return search_by_distance()

    user_location = geojson.Point((user_lon, user_lat))
    query = {
        "luogo.coordinates": {
            "$near": {
                "$geometry": {
                    "type": "Point",
                    "coordinates": [user_lon, user_lat]
                },
                "$maxDistance": max_distance
            }
        }
    }
    results = list(collection.find(query))

    if results:
        # Filtra i risultati per assicurarsi che le location abbiano posti disponibili
        available_concerts = [result for result in results if result["luogo"][0]["posti"]["numero_posti"] > 0]
        if available_concerts:
            choice = show_avariable_concerts(available_concerts)
            if choice == 0:
                return search_by_distance()
            view_details(available_concerts[choice - 1])
            date_choice = int(input("\n0 - Indietro\nSeleziona una data: \n"))
            if date_choice != 0:
                purchase_page(available_concerts[choice - 1])
        else:
            print("Nessun concerto trovato vicino a te con biglietti disponibili.")
            time.sleep(2)
    else:
        print("Nessun concerto trovato vicino a te.")
        time.sleep(2)


def exit_program():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("uscita dal programma")
    time.sleep(1)
