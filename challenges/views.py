from django.shortcuts import render
from django.http import  Http404,HttpResponse, HttpResponseNotFound , HttpResponseRedirect
from django.urls import reverse



monthly_challenges={
    "january":"Praise the Lord on january",
    "febuary":"Praise the Lord on Febuary",
    "march": None,
    "april":"Praise the Lord on april",
    "may":"Praise the Lord on may",
    "june":"Praise the Lord on june",
    "july":None,
    "August":"Praise the Lord on Augost",
    "september": None,
    "october":"Praise the Lord on october",
    "november":"Praise the Lord on november",
    "december":None

}

# Create your views here.

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months":months
    })

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
  
    
    if month > len(months):
          raise Http404()
    
    redirect_month = months[month -1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
        
            "text": challenge_text,
            "month_name": month.capitalize()
        })
    except:
          raise Http404()

    