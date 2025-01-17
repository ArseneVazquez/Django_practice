from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect

from datetime import datetime
import calendar


# Create your views here.



incomes = {}
expenses = {}

class IndexView(View):

    def get(self, request):

        total_expenses = sum(list(expenses.values()))
        total_income = sum(list(incomes.values()))

        total_budget = total_income - total_expenses
        month_number = datetime.today().month
        month = calendar.month_name[month_number]

        # if total_expenses > total_income:
        #     total_budget = total_budget * (-1)

        return render(request, "budgety/index.html",{
            "incomes": incomes,
            "expenses": expenses,
            "total_budget": total_budget,
            "total_incomes": sum(incomes.values()),
            "total_expenses" : sum(expenses.values()),
            "month": month
        })

    def post(self, request):
        if request.method == "POST":
            text = request.POST.get("text")
            number = float(request.POST.get("number"))

            if request.POST.get("sign") == "inc":
                incomes[text] = number
            else:
                expenses[text] = number

            return HttpResponseRedirect("/")
        


def index(request):

    if request.method == "POST":
        text = request.POST.get("text")
        number = request.POST.get("number")

        if request.POST.get("sign") == "+":
            incomes[text] = number
        else:
            expenses[text] = number

        return render(request, "budgety/index.html",{
            "incomes": incomes,
            "expenses": expenses
        })
    
def delete(desc, the_list):
    if desc in the_list:
        del the_list[desc]
    return the_list
    
def deleteIncomeData(request, description):
    delete(description, incomes)
    return HttpResponseRedirect("/")

def deleteExpenseData(request, description):
    delete(description, expenses)
    return HttpResponseRedirect("/")
    