from .views import error_page, index, cart, removecart, success_page

from django.urls import path

urlpatterns = [
    path('', index),
    path('cart/', cart),
    path('cart/remove/<int:id>', removecart),
    path('success_page/', success_page, name="success_page"),
    path('error_page/', error_page, name="error_page"),

]
