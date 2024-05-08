from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ContactsView, ProductCreateView, ProductUpdateView, \
    VersionCreateView, ProductDeleteView, CategoriesListView, CategoriesDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>', cache_page(60)(ProductDetailView.as_view()), name='product'),
    path('product_form/', ProductCreateView.as_view(), name='product_form'),
    path('product_form/<int:pk>', ProductUpdateView.as_view(), name='product_edit'),
    path('product_delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
    path('version_form', VersionCreateView.as_view(), name='version_form'),
    path('categories', CategoriesListView.as_view(), name='categories_list'),
    path('category/<int:pk>', CategoriesDetailView.as_view(), name='category')

]
