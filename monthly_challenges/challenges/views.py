from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse 
# Create your views here.

monthly_challenges = {
    "january":"Eat no meat for the entire month!",
    "february":"Walk for atleast 20 minutes every day",
    "march":"Go for swim for 30 minutes",
    "april":"Go to office by using cycle entire month",
    "may":"Practice meditation for atleast 30 minutes",
    "june":"Practice Boxing for 30 minutes",
    "july":"Read 10 pages of book daily",
    "august":"Practice public speaking for 20 minutes a day",
    "september":"Go to gym daily and lift some weights",
    "october":"Go for a run for atleast 30 minutes a day",
    "november":"Daily wake up at 4:00 am in morning",
    "december":"Create a youtube channel and post a video daily about yourself",
}

def index(request):
    all_months = list(monthly_challenges.keys())
    return render(request, 'challenges/index.html', {'all_months':all_months})


def month(request):
    return HttpResponse("This is February")

def monthly_challenge_by_number(request,month):
    months = list(monthly_challenges.keys())
    try:
        
        forward_month = months[month-1]
        # return HttpResponseRedirect('/challenges/'+forward_month)
        redirect_path = reverse("month-challenge", args = [forward_month])
        return HttpResponseRedirect(redirect_path)
    except:
        raise Http404()
    
    


def monthly_challenge(request, month):
    challenge_text = 'No month found'
    
    try:
        challenge_text = monthly_challenges[month]
    except:
        raise Http404()
    
    return render(request,"challenges/challenge.html",{'month':month, 'challenge_text':challenge_text})
