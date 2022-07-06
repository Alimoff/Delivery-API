from django.contrib import admin
from .models import Orders, Food, Region, Cook, Taxis

# Register your models here.


admin.site.register(Orders)
admin.site.register(Food)
admin.site.register(Region)
admin.site.register(Cook)
admin.site.register(Taxis)
