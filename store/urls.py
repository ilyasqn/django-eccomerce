from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
	path('', views.store, name='store'),
	path('cart/', views.cart, name='cart'),
	path('checkout/', views.checkout, name='checkout'),
    path('update_item/', views.update_item, name='update_item')
]
