from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from catalog.models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/index.html'
    context_object_name = 'object_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'BitStore - Каталог'
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'BitStore - Товар'
        return context


class ContactsView(View):
    template_name = 'catalog/contacts.html'

    def get(self, request, *args, **kwargs):
        context = {
            'title': 'BitStore - Контакты',
            'title_1': 'Контакты',
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(name, phone, message)

        context = {
            'title': 'BitStore - Контакты',
            'title_1': 'Контакты',
        }
        return render(request, self.template_name, context)

# def index(request):
#     products_list = Product.objects.all()
#
#     context = {
#         'object_list': products_list,
#         'title': 'BitStore - Каталог',
#     }
#     return render(request, 'catalog/index.html', context)


# def contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         print(name, phone, message)
#
#     context = {
#         'title': 'BitStore - Контакты',
#         'title_1': 'Контакты',
#     }
#
#     return render(request, 'catalog/contacts.html', context)


# def product(request, pk):
#     products_list = Product.objects.get(pk=pk)
#
#     context = {
#         'object_list': products_list,
#         'title': 'BitStore - Товар',
#     }
#     return render(request, 'catalog/product.html', context)
