from django.urls import path
from . import views


urlpatterns = [
    path("", views.IndexView.as_view()),
    path("delete_income/<str:description>/", views.deleteIncomeData, name="delete_income"),
    path("delete_expense/<str:description>/", views.deleteExpenseData, name="delete_expense")
]
 