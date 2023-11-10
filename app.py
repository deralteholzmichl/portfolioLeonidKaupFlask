from flask import Flask

from Ticket import Ticket

from functools import reduce

from math import sqrt
from functools import reduce

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Wilkommen bei der Fussballspiel reservierung'


@app.route('/anzahlFans/<auswarts>/<heim>')
def show_game(auswarts, heim):
    insgesammt = int(auswarts) + int(heim)
    return 'Insgesammt ' + str(insgesammt) + ' Leute werden das Spiel besuchen'


@app.route('/addTicket/<Name>')
def addTicket(Name):
    file = open('output.txt', 'w')
    file.write("Neues Ticket von " + Name)
    file.close()
    return 'Neues Ticket von ' + Name + ' wurde hinzugefügt'

@app.route('/getCategories/')
def getATuple():
    katerogien = ("Oberrang", "Mittelrang", "Unterrang")
    return katerogien

@app.route('/createTicket/<Name>/<StadionOrt>/<Preis>')
def createTicket(Name,StadionOrt,Preis):
    ticket = Ticket(Name, StadionOrt, Preis)
    return ticket.__str__()

@app.route('/berechneTicketpreis/<AlleEinnahmen>/<AnzahlTickets>')
def calculatePrice(AlleEinnahmen,AnzahlTickets):
    return berechneDurchschnittlicherPreis(AlleEinnahmen,AnzahlTickets)

@app.route('/rechneAlleTicketsZusammen/')
def calculateAllTickets():
    return str(sum([1,2,3,4,5,5,3,3,24,5,6,7,8,9,9,9,9,9,9,9,9,9,9,9,9]))

@app.route('/sortiereTicketPreise/')
def sortTicketCategories():
    list = [{'price': 200,'name':'tribuene1'},{'price': 150,'name':'tribuene2'},{'price': 90,'name':'oberrang'},{'price': 600,'name':'Unterrang'}]
    len = list.__len__()
    for i in range(0,len):
        for j in range(0,len):
            if list[i]['price'] < list[j]['price']:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
    return str(list)

@app.route('/sortiereTicketPreiseFunktional/')
def sortTicketCategoriesFunctional():
    tickets = [{'price': 200, 'name': 'tribuene1'}, {'price': 150, 'name': 'tribuene2'}, {'price': 90, 'name': 'oberrang'}, {'price': 600, 'name': 'Unterrang'}]
    sorted_tickets = sortiereDieTickets(tickets)
    return str(sorted_tickets)

def sortiereDieTickets(list):
    return sorted(list, key=lambda ticket: ticket['price'])


def berechneDurchschnittlicherPreis(AlleEinnahmen,AnzahlTickets):
    return str(int(AlleEinnahmen) / int(AnzahlTickets))

def sortierelisteAusKategorie(list,kategorie):
    return [ticket for ticket in list if ticket['name'] == kategorie]

def berechneDurchschnittlicherPreis(list,anzahlTickets):
    sum = 0
    for ticket in list:
        sum += ticket['price']
    return sum / anzahlTickets

@app.route('/berechnerDurchscnittlicherPreisProKategorie/<Kategorie>')
def berechnerDurchscnittlicherPreisProKategorie(Kategorie):
    tickets = [{'price': 200, 'name': 'tribuene1'}, {'price': 150, 'name': 'tribuene2'}, {'price': 90, 'name': 'oberrang'}, {'price': 600, 'name': 'Unterrang'}, {'price': 550, 'name': 'Unterrang'}, {'price': 710, 'name': 'Unterrang'}, {'price': 602, 'name': 'Unterrang'}]
    ticketsAusKategorie = sortierelisteAusKategorie(tickets, Kategorie)
    durchschnittsPreis = berechneDurchschnittlicherPreis(ticketsAusKategorie,ticketsAusKategorie.__len__())
    return str(durchschnittsPreis)

@app.route('/fuehreTicketBerechnungDurch/<Berechnung>')
def makeCalculaion(Berechnung):
    tickets = [{'price': 200, 'name': 'tribuene1'}, {'price': 150, 'name': 'tribuene2'}, {'price': 90, 'name': 'oberrang'}, {'price': 600, 'name': 'Unterrang'}, {'price': 550, 'name': 'Unterrang'}, {'price': 710, 'name': 'Unterrang'}, {'price': 602, 'name': 'Unterrang'}]
    if Berechnung == "PotenziellerUmsatz":
        return caluclate(potenziellerUmsatz,tickets)
    elif Berechnung == "AnzahlFreierKategorien":
        return caluclate(anzalFreierKategorien,tickets)
    else:
        return "Berechnung nicht gefunden"

def caluclate(operation,list):
    return operation(list)

def potenziellerUmsatz(list):
    sum = 0
    for ticket in list:
        sum += ticket['price']
    return str(sum)

def anzalFreierKategorien(list):
    neueliste = []
    for ticket in list:
        if ticket['name'] not in neueliste:
            neueliste.append(ticket['name'])
    return str(neueliste.__len__())

def apply_function_to_list(func, input_list):
    result = []
    for ticket in input_list:
        result.append(func(ticket['price']))
    return result

@app.route('/transform_numbers/')
def transformNumbers():
    tickets = [{'price': 200, 'name': 'tribuene1'}, {'price': 150, 'name': 'tribuene2'}, {'price': 90, 'name': 'oberrang'}, {'price': 600, 'name': 'Unterrang'}, {'price': 550, 'name': 'Unterrang'}, {'price': 710, 'name': 'Unterrang'}, {'price': 602, 'name': 'Unterrang'}]

    def square(x):
        return x * x

    squared_numbers = apply_function_to_list(square, tickets)

    return f"Ursprüngliche TicketPreise: {tickets}<br>Quadrierte TicketPreise: {squared_numbers}"

def apply_custom_rating_function(rating_function):
    def calculate_rating(ticket):
        return rating_function(ticket)
    return calculate_rating

@app.route('/custom_ticket_rating/')
def custom_ticket_rating():

    ticket_data = [
        {'name': 'Ticket A', 'price': 50, 'available_tickets': 100},
        {'name': 'Ticket B', 'price': 100, 'available_tickets': 50},
        {'name': 'Ticket C', 'price': 30, 'available_tickets': 200},
    ]

    def custom_rating(ticket):
        return (ticket['price'] * 0.2) + (ticket['available_tickets'] * 0.5)

    calculate_custom_rating = apply_custom_rating_function(custom_rating)
    rating_results = [calculate_custom_rating(ticket) for ticket in ticket_data]

    return f"Bewertungsergebnisse:<br>{rating_results}"

@app.route('/transform_numbers_lambda/')
def transformNumbersMitLambda():
    tickets = [{'price': 200, 'name': 'tribuene1'}, {'price': 150, 'name': 'tribuene2'}, {'price': 90, 'name': 'oberrang'}, {'price': 600, 'name': 'Unterrang'}, {'price': 550, 'name': 'Unterrang'}, {'price': 710, 'name': 'Unterrang'}, {'price': 602, 'name': 'Unterrang'}]

    # Hier verwenden wir einen Lambda-Ausdruck, um die Ticketpreise zu quadrieren
    square = lambda x: x**2
    squared_numbers = [square(ticket['price']) for ticket in tickets]

    return f"Ursprüngliche TicketPreise: {tickets}<br>Quadrierte TicketPreise: {squared_numbers}"


# Flask-Endpunkt zur Berechnung des durchschnittlichen Ticketpreises mit Lambda-Ausdrücken
@app.route('/lambda2/<kategorie>')
def lambda2(kategorie):
    fußballtickets = [
        {'name': 'Ticket A', 'preis': 50, 'kategorie': 'Oberrang'},
        {'name': 'Ticket B', 'preis': 100, 'kategorie': 'Mittelrang'},
        {'name': 'Ticket C', 'preis': 30, 'kategorie': 'Oberrang'},
        {'name': 'Ticket D', 'preis': 70, 'kategorie': 'Unterrang'},
        {'name': 'Ticket E', 'preis': 90, 'kategorie': 'Mittelrang'},
    ]
    preis_berechnen = lambda ticket: ticket['preis'] if ticket['kategorie'] == kategorie else 0

    tickets_der_kategorie = list(filter(lambda ticket: ticket['kategorie'] == kategorie, fußballtickets))

    if not tickets_der_kategorie:
        return f'Keine Tickets in der Kategorie {kategorie} gefunden.'

    durchschnittspreis = sum(map(preis_berechnen, tickets_der_kategorie)) / len(tickets_der_kategorie)

    return f'Der durchschnittliche Preis für Tickets in der Kategorie {kategorie} beträgt {durchschnittspreis}.'

@app.route('/lambda3')
def lambda3():
    fußballtickets = [
        {'name': 'Ticket A', 'preis': 50, 'kategorie': 'Oberrang'},
        {'name': 'Ticket B', 'preis': 100, 'kategorie': 'Mittelrang'},
        {'name': 'Ticket C', 'preis': 30, 'kategorie': 'Oberrang'},
        {'name': 'Ticket D', 'preis': 70, 'kategorie': 'Unterrang'},
        {'name': 'Ticket E', 'preis': 90, 'kategorie': 'Mittelrang'},
    ]
    sortierte_tickets = sorted(fußballtickets, key=lambda ticket: ticket['preis'])
    return str(sortierte_tickets)

@app.route('/lambda4')
def lambda4():
    fußballtickets = [
        {'name': 'Ticket A', 'preis': 50, 'kategorie': 'Oberrang'},
        {'name': 'Ticket B', 'preis': 100, 'kategorie': 'Mittelrang'},
        {'name': 'Ticket C', 'preis': 30, 'kategorie': 'Oberrang'},
        {'name': 'Ticket D', 'preis': 70, 'kategorie': 'Unterrang'},
        {'name': 'Ticket E', 'preis': 90, 'kategorie': 'Mittelrang'},
    ]
    sortierte_tickets = sorted(fußballtickets, key=lambda ticket: ticket['kategorie'])
    return str(sortierte_tickets)


@app.route('/map')
def mapExample():
    preiskategorein = [200, 50, 10, 11, 54]

    return str(list(map(square, preiskategorein)))

def square(x):
    return x * x

@app.route('/filter')
def filterExample():
    preiskategorien = [200, 50, 10, 11, 54]
    return  str(list(filter(is_even, preiskategorien)))

def is_even(x):
    return x % 2 == 0

@app.route('/reduce')
def reduceExample():
    preiskategorien = [200, 50, 10, 11, 54]
    return str(reduce(add, preiskategorien))

def add(x, y):
    return x + y

@app.route('/kombo')
def kombinationVonDem():
    preiskategorien = [200, 50, 10, 11, 54]
    result = reduce(lambda x, y: x + y, map(process_data, filter(lambda x: x < 100, preiskategorien)))
    return str(result)

def process_data(x):
    if x % 2 == 0:
        return sqrt(x)
    else:
        return x

@app.route('/komplexKombo')
def komplexKombo():
    fussballTickets = [
{'product': 'Ticket A', 'price': 50.0, 'quantity': 2},
{'product': 'Ticket B', 'price': 75.0, 'quantity': 3},
{'product': 'VIP Ticket', 'price': 200.0, 'quantity': 1}]
    return str(reduce(aggregate_total, map(calculate_ticket_total, fussballTickets)))

def calculate_ticket_total(ticket):
    return ticket['price'] * ticket['quantity']

def aggregate_total(total, ticket):
    return total + calculate_ticket_total(ticket)

@app.route('/refactoringOne')
def refactoring1():
    ticketPreis = 10
    # Unübersichtlicher Code
    p(ticketPreis)
    # Verbesserter Code mit Refactoring-Techniken
    double(ticketPreis)
    return('done')

# Unübersichtlicher Code
def p(x):
    return x * 2

total = 0
for i in range(1, 6):
    total += p(i)

# Verbesserter Code mit Refactoring-Techniken
def double(x):
    return x * 2

@app.route('/refactoringTwo')
def refactoringTwo():
    x(5,2)
    calculate_total(5,2)
    return('done')
# Unübersichtlicher Code
def x(a, b):
    t = 0
    for i in range(a):
        t += i * b
    return t

# Verbesserter Code mit Refactoring-Techniken
def calculate_total(a, b):
    total = 0
    for number in range(a):
        total += number * b
    return total

@app.route('/refactoringThree')
def refactoringThree():
    sell_ticket1("VIP")
    sell_ticket2("Standard")
    return ('done')

#ursprünglicher Code
def calculate_ticket_price1(base_price, discount):
    return base_price - (base_price * discount)

def sell_ticket1(ticket_type):
    if ticket_type == "VIP":
        base_price = 100
        discount = 0.2
    else:
        base_price = 50
        discount = 0.1
    return calculate_ticket_price1(base_price, discount)

#refacdored code
def calculate_ticket_price2(base_price, discount):
    return base_price - (base_price * discount)

def determine_ticket_details2(ticket_type):
    if ticket_type == "VIP":
        return 100, 0.2
    else:
        return 50, 0.1

def sell_ticket2(ticket_type):
    base_price, discount = determine_ticket_details2(ticket_type)
    return calculate_ticket_price2(base_price, discount)

if __name__ == '__main__':
    app.run()
