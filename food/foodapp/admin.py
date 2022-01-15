from django.contrib import admin
from . models import FoodItem
# Register your models here.
class FoodAdmin(admin.ModelAdmin):
    list_filter=('Type',)
    search_fields=('Name',)
    ordering=('Vitamin_Present','Name')
    list_display=('Name','Vitamin_Present')
admin.site.register(FoodItem,FoodAdmin)
