import os
import time
from pymongo import MongoClient


def start_client():
    try:
        client = MongoClient('mongodb+srv://mongodb-ele.xku5epx.mongodb.net/')
        db = client.get_database("Concerti")
        global collection
        collection = db.get_collection("concerti")
        print(collection.name)
        return collection
    except Exception:
        print(Exception)


def exit_program(coll):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("uscita dal programma")
    time.sleep(1)


def search_concert(coll):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("cerca per concerto")
    time.sleep(1)


def search_artist(coll):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("cerca per artista")
    time.sleep(1)


def search_by_date(coll):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("cerca per intervallo di date")
    time.sleep(1)


def search_by_distance(coll):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("ricerca per distanza")
    time.sleep(1)
