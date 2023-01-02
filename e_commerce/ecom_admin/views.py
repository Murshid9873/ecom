from django.shortcuts import render

# Create your views here.

def approve_seller(request):
    return render(request, 'ecom_admintemplates/approve_seller.html')

def home(request):
    return render(request, 'ecom_admintemplates/home.html')

def view_customer(request):
    return render(request, 'ecom_admintemplates/view_customer.html')

def view_seller(request):
    return render(request, 'ecom_admintemplates/view_seller.html')
