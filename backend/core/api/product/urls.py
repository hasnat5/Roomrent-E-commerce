from django.urls import path
from . import views

urlpatterns = [
    path('',views.listProduct),
    path('add/',views.createProduct),
    path('<str:product_name>',views.getProduct),
    path('<str:product_name>/update',views.updateProduct),
    path('<str:product_name>/delete',views.deleteProduct),
]
