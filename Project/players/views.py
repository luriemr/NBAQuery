from django.shortcuts import render
from .models import players
from django.views import View


app_name = 'players'

def playerlist(request):
    statsReg = list(players.objects.filter(pts__gt=-1).order_by('-year').values())
    return render(request, 'djangotest.html', {'stats': statsReg})


            
    
