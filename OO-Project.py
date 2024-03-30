# museum.py
class Museum:
   def __init__(self):
       self.artworks = []
       self.exhibitions = []
       self.visitors = []
       self.ticket_sales = []


   def add_artwork(self, artwork):
       self.artworks.append(artwork)


   def open_exhibition(self, exhibition):
       self.exhibitions.append(exhibition)


   def sell_ticket(self, ticket):
       self.ticket_sales.append(ticket)


   def display_receipt(self, ticket):
       # Display receipt logic goes here
       pass


# artwork.py
class Artwork:
   def __init__(self, title, artist, date_of_creation, historical_significance, location):
       self.title = title
       self.artist = artist
       self.date_of_creation = date_of_creation
       self.historical_significance = historical_significance
       self.location = location


# exhibition.py
class Exhibition:
   def __init__(self, title, location, duration):
       self.title = title
       self.location = location
       self.duration = duration


# visitor.py
class Visitor:
   def __init__(self, name, age, category):
       self.name = name
       self.age = age
       self.category = category


# ticket.py
class Ticket:
   def __init__(self, event, price, vat, total_price):
       self.event = event
       self.price = price
       self.vat = vat
       self.total_price = total_price