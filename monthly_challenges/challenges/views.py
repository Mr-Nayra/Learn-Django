from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges ={
    'january':"Eat no meat for the entire month!",
    'february': "It's feb now",
    'march':"It's March now",
    'april':"It's april now",
    'may':"It's may",
    'june':"It's june now",
    'july': "It's july now",
    'august': "It's august baby",
    'september': "It's september now",
    'october':"It's october now",
    'november':"It's november now",
    'december':"It's december now"
}

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    
    for month in months:
        month_path=reverse("month-challenge", args=[month])
        list_items += f'<li><a href="{month_path}">{month.capitalize()}</a></li>'

    response_data= f'<ul>{list_items}</ul>'
    return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
    
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) #/challenge/january
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")