from django.shortcuts import render

def index(reguest):
    if reguest.mehtod == 'POST':
        name = reguest.mehtod.POST.get('name')
        email = reguest.mehtod.POST.get('email')
        print(f'{name} {email}')
    return render(reguest, 'main/index.html')
