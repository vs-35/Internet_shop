from django.shortcuts import render

def index(request):
    if request.method == 'POST':
        name = request.method.POST.get('name')
        email = request.method.POST.get('email')
        print(f'{name} {email}')
    return render(request, 'main/index.html')


def home(request):
    return render(request, 'main/home.html')


def product(request, product_id):
    product = Products.objects.get(pk=product_id)
    context = {
        'product': product,
        'contacts_active': 'text-white',
        'home_active': 'text-white',
        'category_active': 'active',
    }
    return render(request, 'catalog/product.html', context)