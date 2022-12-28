from django.urls import path
from .component.landingPage import landingPage
from .component.landingPage import ProductListview
urlpatterns = [
    path('',landingPage)
]
