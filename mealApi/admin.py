from django.contrib import admin
from .models import Meal

# Register your models here.

class MealAdmin(admin.ModelAdmin):
    list_display = ('date', 'service_type')



admin.site.register(Meal, MealAdmin)