from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Flight, Airport, Passenger

# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })

def flight(request, flight_id):
	existing_flight = Flight.objects.get(id=flight_id)
	passengers = existing_flight.passengers.all()  # all passengers in the particular flight
	non_passengers = Passenger.objects.exclude(flights=existing_flight).all()  # exclude existing passengers in the particular flight
	return render(request, "flights/flight.html", {
		"flight": existing_flight,
		"passengers": passengers,
		"non_passengers": non_passengers
	})

def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)

        passenger_id = int(request.POST["passenger"])

        passenger = Passenger.objects.get(pk=passenger_id)

        passenger.flights.add(flight)

        return HttpResponseRedirect(reverse("flights:flight", args=(flight.id,)))