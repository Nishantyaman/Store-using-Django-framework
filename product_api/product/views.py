from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import render
from .forms import product_form
from .models import product_info
from .serializers import product_infoSerializer
from django.http import HttpResponse
from django.core import serializers
from django.urls import reverse
from django.http import HttpResponseRedirect
import json

def index(request):
	productss=product_info.objects.all()
	leads_as_json = serializers.serialize('json', productss)
	return HttpResponse(leads_as_json, content_type='json')

def addform(request):

	if request.method == "POST":
		title = request.POST["title"]
		price = request.POST["price"]
		description = request.POST["description"]
		category = request.POST["category"]

		products_info = product_info(title=title,price=price,description=description,category=category,image='C:/Users/NIshant/djangop/product_api/flask.png')
		products_info.save()
		return HttpResponseRedirect(reverse('home'))
	else:
		form=product_form()
		return render(request, 'product/add.html',{form:'form'})

def homeform(request):
	return render(request,'product/home.html')

def readable_format(request):
	product_data=[]
	productss=product_info.objects.values()
	list_result = [entry for entry in productss]
	print(list_result[0])

	for products in list_result:
			product_d = {
				'title': products['title'],
				'price': products['price'],
				'description': products['description'],
				'category': products['category']
			}

			product_data.append(product_d)

	print(product_data)

	return render(request,'product/details.html',{'product_data':product_data})

	
