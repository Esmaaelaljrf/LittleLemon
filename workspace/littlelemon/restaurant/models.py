from django.db import models
import datetime
# Create your models here.
class Booking(models.Model):
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField()
    BookingDate = models.DateField(default=datetime.date.today)

class Menu(models.Model):
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.IntegerField()

    def __str__(self):
        return f'{self.Title} : {str(self.Price)}'
# # Create your models here.
# class Booking(models.Model):
#     name = models.CharField(max_length=255)
#     no_of_guests = models.IntegerField()
#     booking_date = models.DateField()

# class Menu(models.Model):
#     title = models.CharField(max_length=255)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     inventory = models.IntegerField()
#     def get_item(self):
#         return f'{self.title} : {str(self.price)}'
   