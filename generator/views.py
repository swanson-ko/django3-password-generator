from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
# This references html files in "templates/generator" folder

def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')    

"""
since there was another page or path, we are returning a response to the browser
"""
def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    length = int(request.GET.get('length', 12))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password':thepassword})
