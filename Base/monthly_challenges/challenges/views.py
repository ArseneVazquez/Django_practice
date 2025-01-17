from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges ={
    "january": "this is january",
    "febuary": "this is febuary",
    "march": "this is march",
    "april": "this is april",
    "may": "this is may",
    "june": "this is june",
    "july": "this is july",
    "august": "this is august",
    "september": "this is september",
    "october": "this is october",
    "november": "this is november",
    "december": None
}

# Create your views here.
def index(request):
    months = list(monthly_challenges.keys())
        
    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("<h1>Invalid month</h1>")
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def mothly_challenge(request, month):

    try:
        challenge_text = monthly_challenges[month]
        return render(request ,"challenges/challenge.html", {
            "text" : challenge_text,
            "month_name": month
        })
    except:
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)
    
