from django.urls import path
from . import views
from django.conf.urls import handler500

urlpatterns = [
    path('',views.listUser),
    path('create/',views.createUser),
    path('<str:username>/',views.getUser),
    path('<str:username>/update',views.updateUser),
    path('<str:username>/delete',views.deleteUser),
]

