from django.shortcuts import render

def index(request):
    if request.method == 'POST':
        name = request.method.POST.get('name')
        email = request.method.POST.get('email')
        print(f'{name} {email}')
    return render(request, 'main/index.html')


def home(request):
    return render(request, 'main/home.html')