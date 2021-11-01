from django.contrib import admin
from .models import Card

# Register your models here.
@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'link')
    list_filter = ('title', 'description',)
    search_fields = ('title', 'description',)