from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Seat

def home(request):
    seats = Seat.objects.all()
    return render(request, 'reservation/home.html', {'seats': seats})

def book_seats(request):
    if request.method == 'POST':
        # Get the number of seats requested
        num_seats = int(request.POST.get('num_seats'))
        
        # Get available seats ordered by row_number and seat_number
        available_seats = Seat.objects.filter(status=False).order_by('row_number', 'seat_number')
        
        if available_seats.count() < num_seats:
            # If there aren't enough available seats, send an error
            return JsonResponse({'error': 'Not enough seats available!'})
        
        booked_seats = []
        
        # Book the seats by setting their status to True
        for seat in available_seats[:num_seats]:
            seat.status = True
            seat.save()
            booked_seats.append(seat.seat_number)
        
        # Return the updated list of booked seats as a JSON response
        return JsonResponse({'success': True, 'booked_seats': booked_seats})
    else:
        # If the method is not POST, just redirect back to the home page
        return redirect('home')
