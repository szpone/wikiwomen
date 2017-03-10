from django.contrib import admin
from .models import Scientists, Specialization
# Register your models here.

@admin.register(Scientists)
class ScientistsAdmin(admin.ModelAdmin):
    list_display = ("name", "gender", "link", "extra_info")

@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ("name", )

