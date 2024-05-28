from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound , HttpResponseRedirect
from django.urls import reverse


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
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("THis month is not suported!!!!")

    