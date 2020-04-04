from django.db import models


# Create your models here.


class Booking(models.Model):
	book_ref = models.AutoField(primary_key=True)
	book_date = models.DateTimeField()
	total_amount = models.FloatField(null=False)

	def __str__(self):
		return f'{self.book_ref} - {self.book_date}'


class Aircraft(models.Model):

	aircraft_code = models.PositiveIntegerField(primary_key=True)
	model = models.CharField(max_length=100)
	range = models.PositiveIntegerField()

	def __str__(self):
		return f'{self.aircraft_code} - {self.model}'


class Airport(models.Model):
	airport_code = models.AutoField(primary_key=True)
	airport_name = models.CharField(max_length=200)
	city = models.CharField(max_length=200)
	coordinates = models.TextField(max_length=100)

	def __str__(self):
		return f'{self.airport_code} - {self.airport_name} - {self.city}'


class Flight(models.Model):

	flight_id = models.PositiveIntegerField(primary_key=True)
	flight_no = models.PositiveIntegerField(null=False)
	scheduled_departure = models.TimeField()
	scheduled_arrival = models.TimeField()
	departure_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departure_airport')
	arrival_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrival_airport')
	status = models.TextField()
	aircraft_code = models.ForeignKey(Aircraft, on_delete=models.CASCADE)
	actual_departure = models.TimeField()
	actual_arrival = models.TimeField()

	def __str__(self):
		return f'{self.flight_no} - {self.actual_departure} - {self.actual_arrival} ' \
				f'- {self.departure_airport} - {self.arrival_airport}'


class Seat(models.Model):
	aircraft_code = models.ForeignKey(Aircraft, on_delete=models.CASCADE)
	seat_no = models.CharField(null=False, max_length=3)
	fare_conditions = models.CharField(max_length=250, null=False)

	def __str__(self):
		return f'{self.aircraft_code} - {self.seat_no}'


class Ticket(models.Model):
	tickets_no = models.AutoField(primary_key=True)
	book_ref = models.ForeignKey(Booking, on_delete=models.CASCADE)
	passenger_id = models.PositiveIntegerField(null=False)
	passenger_name = models.CharField(max_length=250, null=False)
	contact_data = models.CharField(max_length=250, null=False)

	def __str__(self):
		return f'{self.tickets_no} - {self.passenger_name}'


class TicketFlight(models.Model):
	ticket_no = models.ForeignKey(Ticket, on_delete=models.CASCADE)
	flight_id = models.ForeignKey(Flight, on_delete=models.CASCADE)
	fare_conditions = models.ForeignKey(Seat, on_delete=models.CASCADE)
	amount = models.PositiveIntegerField(null=False)

	def __str__(self):
		return f'{self.flight_id} - {self.fare_conditions}'

	class Meta:
		unique_together = (('ticket_no', 'flight_id'), )


class BoardingPasses(models.Model):
	ticket_no = models.ForeignKey(TicketFlight, on_delete=models.CASCADE, related_name='ticket_no1')
	flight_id = models.ForeignKey(TicketFlight, on_delete=models.CASCADE, related_name='flight_id1')
	boarding_no = models.PositiveIntegerField(null=False)
	seat_no = models.ForeignKey(Seat, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.boarding_no} - {self.seat_no}'

	class Meta:
		unique_together = (('ticket_no', 'flight_id'), )







