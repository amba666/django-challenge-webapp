from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def monthly_challenge(request, month):
    challenge_text = None
    if month =="january":
        challenge_text = "Praise the Lord!"
    elif month == "febuary":
        challenge_text = "Praise the Lord on Febuary"
    elif month == "march":
        challenge_text ="Praise the Lord on March"
    else:
        return HttpResponseNotFound("THis month is not supported!!!")
    return HttpResponse(challenge_text)