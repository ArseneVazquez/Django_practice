from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect
from .models import BudgetModel

from datetime import datetime
import calendar


# Create your views here.

# a function to get budget and check if it's incomes or expenses
def typeOfBudget(isPositive):
    if isPositive:
        incomes = BudgetModel.objects.filter(value__gt=0)

        return incomes
    else:
        depenses = BudgetModel.objects.filter(value__lte=0)

        return depenses

# A class to save to the Model and get data to the Model

class IndexView(View):


    def get(self, request):

        incomes = typeOfBudget(True)
        expenses = typeOfBudget(False)

        budget_model = list(BudgetModel.objects.all())
        total_budget = sum(budget.value for budget in budget_model)
        month_number = datetime.today().month
        month = calendar.month_name[month_number]

        return render(request, "budgety/index.html",{
            "incomes": incomes,
            "expenses": expenses,
            "total_budget": total_budget,
            "total_incomes": sum(list(income.value for income in incomes)),
            "total_expenses" : sum(list(expense.value for expense in expenses)),
            "month": month
        })

    def post(self, request):
        if request.method == "POST":
            text = request.POST.get("text")
            number = float(request.POST.get("number"))

            if request.POST.get("sign") == "exp":
                number *= -1

            BudgetModel(description=text, value=number).save()

            return HttpResponseRedirect("/")
        


# A function to delete a Data
    
def deleteData(request, pk):
    BudgetModel.objects.get(pk=pk).delete()
    return HttpResponseRedirect("/")
    