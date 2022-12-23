from django.urls import path
from .component import product

urlpatterns = [
    path('',product.listProduct, name="list"),
    path('add/',product.addProduct, name="add"),
    path('<int:id_product>/',product.getProduct, name="get"),
    path('<int:delete_id>/delete/',product.deleteProduct, name="delete"),
    path('<int:update_id>/update/',product.updateProduct, name="update"),
]
