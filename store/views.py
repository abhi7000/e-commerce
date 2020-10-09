from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact
# Create your views here.
def index(request):
	product=Product.objects.all()
	# # product_names=[]
	# # for i in item:
	# # 	product_names.append(i.product_name)
	# print(item)
	# allproducts=[	[item,len(item)],
	# 				[item,len(item)]
	# 			]
	cat_prod=[]
	catProd=Product.objects.values('sub_cat')
	cats={var['sub_cat'] for var in catProd}
	for cat in cats:
		prod=Product.objects.filter(sub_cat=cat)
		cat_prod.append(prod)

	param={
			"allproduct":cat_prod,
			}
	return render(request,'store/index.html',param)
def search(request):
	return render(request,'store/search.html')

def about(request):
	return render(request,'store/about.html')

def contactus(request):
	# point to be noted
	# post method used here uses ""name"" for fetching data not ""id""
	if(request.method=="POST"):
		name=request.POST.get('name','')
		email=request.POST.get('email','')
		phone=request.POST.get('phone','')
		desc=request.POST.get('desc','')
		print(name,email,phone,desc)
		
		a=Contact(name=name,email=email,phone=phone,desc=desc)
		a.save()


	return render(request,'store/contactus.html')

def productview(request,qkid):
	product=Product.objects.filter(id=qkid)
	return render(request,'store/productview.html',{'product':product[0]})

def checkout(request):
	return render(request,'store/checkout.html')

def cartview(request):
	return render(request,'store/cartview.html')

