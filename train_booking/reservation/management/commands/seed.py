from django.core.management.base import BaseCommand
from reservation.models import Seat

class Command(BaseCommand):
    help = 'Seed the database with initial seat data'

    def handle(self, *args, **kwargs):
        Seat.objects.all().delete()  # Clear existing data
        seat_number = 1
        for row in range(1, 13):  # 12 rows
            seats_in_row = 7 if row < 12 else 3
            for seat in range(1, seats_in_row + 1):
                Seat.objects.create(
                    seat_number=f"R{row}S{seat}",
                    row_number=row,
                    status=False
                )
        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))
