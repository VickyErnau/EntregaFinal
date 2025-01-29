from django.contrib import admin

# Register your models here.

from .models import  Posteo

@admin.register(Posteo)
class PosteoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'create_date', 'update_date')
    search_fields = ('titulo', 'resumen', 'texto')
    