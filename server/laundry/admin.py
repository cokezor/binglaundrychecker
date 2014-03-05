from django.contrib import admin
from laundry.models import Building, LaundryRoom, Machine

admin.site.register(Building)
admin.site.register(LaundryRoom)
admin.site.register(Machine)

# Register your models here.
