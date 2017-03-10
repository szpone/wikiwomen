from django.contrib import admin
from .models import Scientist
# Register your models here.

@admin.register(Scientist)
class ScientistAdmin(admin.ModelAdmin):
    list_display = ("women_number", "men_number", "specialization")
