from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges ={
    'january':"Eat only meat for the entire month!",
    'february': "Run marathon",
    'march':"Learn react",
    'april':"Learn Django",
    'may':"Learn C++",
    'june':"Learn Blockchain Development",
    'july': "Get two jobs",
    'august': "Eat only meat for the entire month!",
    'september': "Learn React-Native",
    'october':"Learn BlockChain Development",
    'november':"Earm 5 lakhs",
    'december': None
}

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    
    return render(request, "challenges/index.html", {
        "months" : months
    })

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        raise Http404()
    
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) #/challenge/january
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html",{
            "text": challenge_text,
            "month": month
        })
    except:
        raise Http404()