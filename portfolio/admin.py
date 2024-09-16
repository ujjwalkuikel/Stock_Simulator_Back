from django.contrib import admin
from .models import Portfolio, PortfolioItem, Transaction

# Register your models here.
class PortfolioAdmin(admin.ModelAdmin):
    model = Portfolio

admin.site.register(Portfolio, PortfolioAdmin)

class PortfolioItemAdmin(admin.ModelAdmin):
    model = PortfolioItem

admin.site.register(PortfolioItem, PortfolioItemAdmin)

class TransactionAdmin(admin.ModelAdmin):
    model = Transaction

admin.site.register(Transaction, TransactionAdmin)