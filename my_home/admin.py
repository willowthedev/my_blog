from django.contrib import admin
from .models import Header, Card

# Register your models here.
@admin.register(Header)
class HeaderAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle')
    list_filter = ('title', 'subtitle')
    search_fields = ('title', 'subtitle')

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'link')
    list_filter = ('title', 'description',)
    search_fields = ('title', 'description',)