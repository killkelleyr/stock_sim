from django.contrib import admin
from .models import Portfolio, Position

class PortfolioAdmin(admin.ModelAdmin):
    fields = ['user','balance']
    list_display = ['user','balance']

class PositionAdmin(admin.ModelAdmin):
    fields = ['name', 'symbol', 'qantity', 'price', 'portfolio']
    list_display = ['symbol', 'price']

admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Position, PositionAdmin)