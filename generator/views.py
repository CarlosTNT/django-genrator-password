from django.shortcuts import render
from random import choice

def about(request):
    return render(request,'generator/about.html')

def home(request):
    return render(request,'generator/home.html')

def password(request):

    characters = list('qwertyuiopasdfghjklzxcvbnm')
    generated_password = ''

    lenght = int(request.GET.get('lenght'))

    if request.GET.get('uppercase'):
        characters.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM '))

    if request.GET.get('numbers'):
        characters.extend(list('9876543210'))

    if request.GET.get('special'):
        characters.extend(list('¿¡·$%&+*'))

    for x in range(lenght):
        generated_password += choice(characters)

    return render(request,'generator/password.html',{'password':generated_password})

