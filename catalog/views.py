from django.shortcuts import render

from catalog.models import Product


def index(request):
    products_list = Product.objects.all()

    context = {
        'object_list': products_list,
        'title': 'BitStore - Каталог',
    }
    return render(request, 'catalog/index.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(name, phone, message)

    context = {
        'title': 'BitStore - Контакты',
        'title_1': 'Контакты',
    }

    return render(request, 'catalog/contacts.html', context)


def product(request, pk):
    products_list = Product.objects.get(pk=pk)

    context = {
        'object_list': products_list,
        'title': 'BitStore - Товар',
    }
    return render(request, 'catalog/product.html', context)
