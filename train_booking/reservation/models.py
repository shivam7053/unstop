from django.db import models

class Seat(models.Model):
    seat_number = models.CharField(max_length=10, unique=True)  # e.g., R1S1
    row_number = models.IntegerField()
    status = models.BooleanField(default=False)  # False = available, True = booked

    def __str__(self):
        return f"{self.seat_number} - {'Booked' if self.status else 'Available'}"
