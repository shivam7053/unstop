from django.urls import path
from .views import home, book_seats

urlpatterns = [
    path('', home, name='home'),
    path('book/', book_seats, name='book_seats'),
]
