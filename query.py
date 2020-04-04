# python manage.py shell

# from airtrans.models import *

# Flight.objects.all()
# <QuerySet [<Flight: 111 - 17:41:23 - 20:41:25 - 1 - Pulkovo - Saint-Petersburg - 2 - Sheremetevo - Moscow>]>

# Seat.objects.all().filter(aircraft_code='505')
# <QuerySet [<Seat: 505 - Boing - 11A>, <Seat: 505 - Boing - 20C>, <Seat: 505 - Boing - 09B>, <Seat: 505 - Boing - 11B>]>

# BoardingPasses.objects.all().filter(boarding_no='111')
# <QuerySet [<BoardingPasses: 111 - 505 - Boing - 11A>, <BoardingPasses: 111 - 505 - Boing - 20C>]>

# pn = Ticket.objects.all()
# names = [pn[0].passenger_name, pn[1].passenger_name]
# names
# ['Ivan', 'Tamara']

