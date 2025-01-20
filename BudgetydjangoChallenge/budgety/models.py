from django.db import models

# Create your models here.

class BudgetModel(models.Model):
    description = models.CharField(max_length=200)
    value = models.FloatField(max_length=100)

    def __str__(self):
        return f"{self.description} : {self.value}"
    
