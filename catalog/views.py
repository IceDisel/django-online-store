from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from catalog.forms import ProductForm, VersionForm, ProductDeleteForm, ProductModeratorForm
from catalog.models import Product, Version, Category
from catalog.services import get_categories_from_cache, get_category_products_from_cache


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'catalog/index.html'
    context_object_name = 'object_list'
    login_url = 'users:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'BitStore - Каталог'

        context['object_list'] = Product.objects.all()

        for product in context['object_list']:
            product.active_version = Version.objects.filter(product=product, activ_ver=True).last()

        return context


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'BitStore - Товар'
        return context


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')

    def get_form_class(self):
        user = self.request.user

        if user == self.object.owner:
            return ProductForm

        if user.has_perm('catalog.set_published_status') and user.has_perm(
                'catalog.can_edit_description') and user.has_perm('catalog.can_edit_category'):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    form_class = ProductDeleteForm
    success_url = reverse_lazy('catalog:index')


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


class VersionCreateView(LoginRequiredMixin, CreateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:index')


class CategoriesListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'catalog/category_list.html'

    def get_queryset(self):
        return get_categories_from_cache()


class CategoriesDetailView(LoginRequiredMixin, DetailView):
    model = Category
    template_name = 'catalog/category_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'BitStore - Товар'
        context['object_list'] = get_category_products_from_cache(self.kwargs.get('pk'))

        return context
