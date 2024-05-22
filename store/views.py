import json
from django.http import JsonResponse
from django.shortcuts import render
from .models import Product, Order, OrderItem

# Create your views here.


def store(request):
	products = Product.objects.all()
	
	context = {
		'products': products
	}
	return render(request, 'store/store.html', context=context)
def cart(request):
	
	items = []
	order = {'get_cart_total': 0, 'get_cart_quantity': 0}
	
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		
	context = {'items': items, 'order': order}
	return render(request, 'store/cart.html', context=context)
def checkout(request):
	items = []
	order = {'get_cart_total': 0, 'get_cart_quantity': 0}
	
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
	
	context = {'items': items, 'order': order}
	
	return render(request, 'store/checkout.html', context=context)

def update_item(request):
	data = json.loads(request.body)
	productId = data['product_id']
	action = data['action']

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)
	
	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()



	return JsonResponse('Hey legend', safe=False)