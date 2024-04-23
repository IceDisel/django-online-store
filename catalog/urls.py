from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ContactsView, ProductCreateView, ProductUpdateView, VersionCreateView, ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product'),
    path('product_form/', ProductCreateView.as_view(), name='product_form'),
    path('product_form/<int:pk>', ProductUpdateView.as_view(), name='product_edit'),
    path('product_delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
    path('version_form', VersionCreateView.as_view(), name='version_form'),


]
