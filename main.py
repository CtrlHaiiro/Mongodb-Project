import funzioni
import os
import time
from pymongo import MongoClient
import re


def display_menu(coll):
    while True:
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("                Benvenuto!\n"
                  "ecco le opzioni che sono a tua disposizione:\n\n"
                  "| 1- Ricerca per Concerto                     |\n"
                  "| 2- Ricerca per Artista                      |\n"
                  "| 3- Ricerca Concerti vicino a te             |\n"
                  "| 4- Ricerca concerti per intervallo di date  |\n"
                  "| 0- Esci dal programma                       |\n")

            choice = int(input("Inserisci la tua scelta:  "))
            match choice:
                case 1:
                    funzioni.search_concert()
                case 2:
                    funzioni.search_artist()
                case 3:
                    funzioni.search_by_date()
                case 4:
                    funzioni.search_by_distance()
                case 0:
                    funzioni.exit_program()
                    break
                case _:
                    raise ValueError

        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("---- la scelta inserita non è valida ----")
            time.sleep(2)

        except Exception as e:
            print(f"Errore: {e}")


if __name__ == '__main__':
    coll = funzioni.start_client()
    display_menu(coll)
