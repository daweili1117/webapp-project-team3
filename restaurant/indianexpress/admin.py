from django.contrib import admin
from .models import Reservation


# Register your models here.
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'num', 'date', 'time', 'guests', 'requests')


admin.site.register(Reservation ,ReservationAdmin)
