import funzioni
import os


def display_menu(coll):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Benvenuto!\n"
              "ecco le opzioni che sono a tua disposizione:\n"
              "1- Ricerca per Concerto\n"
              "2- Ricerca per Artista\n"
              "3- Ricerca Concerti vicino a te\n"
              "4- Ricerca concerti per intervallo di date\n"
              "5- Esci dal programma\n")

        choice = int(input("Inserisci la tua scelta:  "))
        match choice:
            case 1:
                funzioni.search_concert(coll)
            case 2:
                funzioni.search_artist(coll)
            case 3:
                funzioni.search_by_date(coll)
            case 4:
                funzioni.search_by_distance(coll)
            case 5:
                funzioni.exit_program(coll)
                break


if __name__ == '__main__':
    collection = funzioni.start_client()
    display_menu(collection)

