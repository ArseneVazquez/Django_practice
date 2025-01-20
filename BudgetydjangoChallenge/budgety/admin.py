from django.contrib import admin
from .models import BudgetModel

# Register your models here.

class BudgetModelAdmin(admin.ModelAdmin):
    list_display = ("description", "value")

admin.site.register(BudgetModel, BudgetModelAdmin)
