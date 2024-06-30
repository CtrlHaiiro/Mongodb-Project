import random
import json
from datetime import datetime, timedelta
from faker import Faker

fake = Faker('it_IT')

def generate_random_event():
    seats = generate_random_seats()

    event = {
        "nome": generate_random_name(),
        "artisti": generate_random_artists(),
        "luogo": [
            {
                "tempo": generate_random_tempo(),
                "locale": generate_random_locale(),
                "citta": generate_random_city(),
                "coordinates": {"type": "Point", "coordinates": generate_random_coordinates()},
                "posti": {
                    "prezzo": random.randint(40, 100),
                    "posti": seats,
                    "numero_posti": len(seats),
                }},
            {
                "tempo": generate_random_tempo(),
                "locale": generate_random_locale(),
                "citta": generate_random_city(),
                "coordinates": {"type": "Point", "coordinates": generate_random_coordinates()},
                "posti": {
                    "prezzo": random.randint(40, 100),
                    "posti": seats,
                    "numero_posti": len(seats),
                },
            },
        ],
    }
    return event

def generate_random_name():
    concerti_italiani = [
        "Home Festival",
        "Collisioni Festival",
        "Nextones",
        "Terraforma",
        "Time in Jazz",
        "JazzMi",
        "Seeyousound",
        "Sponz Fest",
        "Umbria Rock Festival",
        "Operaestate Festival",
        "Concerto del Primo Maggio",
        "Estate Romana",
        "Unaltrofestival",
        "Sirene Festival",
        "Polifonic Festival",
        "Club to Club",
        "Firenze Rocks",
        "MI AMI Festival",
        "Festival della Bellezza",
        "Todays Festival",
        "Beach Bum Rock Festival",
        "Ortigia Sound System",
        "Ariano Folkfestival",
        "Festival dei Due Mondi",
        "Locomotive Jazz Festival",
        "Flowers Festival",
        "Festival di Pianoforte",
    ]
    scelta = random.choice(concerti_italiani)
    concerti_italiani.remove(scelta)
    return scelta

def generate_random_artists():
    artisti_italiani = [
        "Lucio Battisti",
        "Eros Ramazzotti",
        "Laura Pausini",
        "Vasco Rossi",
        "Ligabue",
        "Tiziano Ferro",
        "Jovanotti",
        "Zucchero",
        "Gianna Nannini",
        "Eros Ramazzotti",
        "Giorgia",
        "Fiorella Mannoia",
        "Claudio Baglioni",
        "Lucio Dalla",
        "Francesco De Gregori",
        "Antonello Venditti",
        "Gianni Morandi",
        "Renato Zero",
        "Raf",
        "Pino Daniele",
        "Biagio Antonacci",
        "Max Pezzali",
        "Subsonica",
        "Negramaro",
        "Måneskin",
        "Thegiornalisti",
        "Salmo",
        "Achille Lauro",
        "Marracash",
        "Fabrizio Moro",
        "Ultimo",
        "Levante",
        "Alessandra Amoroso",
        "Annalisa",
        "Francesco Renga",
        "Loredana Bertè",
        "Enrico Ruggeri",
        "Mina",
        "Mango",
        "Mia Martini",
        "Matia Bazar",
        "Pino Daniele",
        "Luca Carboni",
        "Rocco Hunt",
        "Caparezza",
        "Elisa",
        "J-Ax",
        "Giusy Ferreri",
        "Paola Turci",
    ]

    num_artists = random.randint(1, 3)
    artists = [random.choice(artisti_italiani) for _ in range(num_artists)]
    return artists

def generate_random_tempo():
    start_date = datetime.now()
    random_date = start_date + timedelta(days=random.randint(1, 365))
    random_time = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}"
    return {
        "data": [random_date.strftime("%Y-%m-%d")],
        "ora": random_time
    }

def generate_random_locale():
    locali_concerti = [
        "Mediolanum Forum",
        "Palalottomatica",
        "Unipol Arena",
        "Pala Alpitour",
        "Arena di Verona",
        "Stadio San Siro",
        "Stadio Olimpico",
        "Teatro Ariston",
        "Auditorium Parco della Musica",
        "Teatro degli Arcimboldi",
        "PalaPartenope",
        "Palazzetto dello Sport",
        "Palasport",
        "Paladozza",
        "Atlantico",
        "Fabrique",
        "Obihall",
        "Estragon",
        "Teatro Regio",
        "Palermo Pride Village"
    ]
    scelta = random.choice(locali_concerti)
    locali_concerti.remove(scelta)
    return scelta

def generate_random_city():
    citta_italiane = [
        "Roma",
        "Milano",
        "Napoli",
        "Torino",
        "Palermo",
        "Genova",
        "Bologna",
        "Firenze",
        "Bari",
        "Catania",
        "Verona",
        "Venezia",
        "Messina",
        "Padova",
        "Trieste",
        "Taranto",
        "Brescia",
        "Parma",
        "Prato",
        "Modena"
    ]
    scelta = random.choice(citta_italiane)
    citta_italiane.remove(scelta)
    return scelta

def generate_random_coordinates():
    return [round(random.uniform(-90, 90), 6),
            round(random.uniform(-30, 30), 6)]

def generate_random_seats():
    seats = []
    num_seats = random.randint(0, 15)
    for i in range(num_seats):
        seats.append(f"{int(i + 1)}")
    return seats

# Genera un evento casuale e lo stampa come JSON
eventi = []
for i in range(1, 15):
    eventi.append(generate_random_event())

with open('database.json', 'w') as file:
    json.dump(eventi, file, indent=4)

print("Evento salvato in 'database.json'")
