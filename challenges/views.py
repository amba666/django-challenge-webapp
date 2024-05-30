from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound , HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string


monthly_challenges={
    "january":"Praise the Lord on january",
    "febuary":"Praise the Lord on Febuary",
    "march":"Praise the Lord on march",
    "april":"Praise the Lord on april",
    "may":"Praise the Lord on may",
    "june":"Praise the Lord on june",
    "july":"Praise the Lord on july",
    "August":"Praise the Lord on Augost",
    "september":"Praise the Lord on september",
    "october":"Praise the Lord on october",
    "november":"Praise the Lord on november",
    "december":"Praise the Lord on december"

}

# Create your views here.

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path =  reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"

    return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound("Invalid Month")
    
    redirect_month = months[month -1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = render_to_string("challenges/challenge.html")
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("THis month is not suported!!!!")

    