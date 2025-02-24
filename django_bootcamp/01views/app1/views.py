from django.shortcuts import render
from django.http import HttpResponse

from datetime import date

# Create your views here.
def home(request):
    return HttpResponse('Helloooooooooo')


def about(request):
    return HttpResponse('ZTM rules.')

def greet_user(request, username):
    return HttpResponse(f'Welcome aboard, {username.title()}!')

def calc_age(request, name, year):
    current_year = date.today().year
    user_age = current_year - year
    return HttpResponse(f'You are {user_age}, {name.title()} :]')
