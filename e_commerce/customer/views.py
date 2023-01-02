from django.shortcuts import render,redirect
from  reseller.models import Product
from . models import cart
from common.models import Customer
from .decorator import auth_customer

# Create your views here.

@auth_customer
def home(request):
    # if 'customer' in request.session:
        products = Product.objects.all() # select * from product
        # products = [
        #  {
        #    seller:2 
        #    product_name : 'laptop'
        #     -------- 
        #  },
        #  
        #    {
        #    seller:2 
        #    product_name : 'bag'
        #     -------- 
        #   }
        # ]
        return render(request, 'customertemplates/home.html', {'product_list': products})
    # else:
    #     return redirect('common:custlo')    

@auth_customer
def product_details(request,pid):
    msg = ''
    product_data = Product.objects.get(id = pid)  # fetching single data from table
    if request.method == 'POST':
        product_id = request.POST['pid']

        item_exist = cart.objects.filter(Product_id = product_id, customer_id = request.session['customer']).exists()
        if not item_exist: # if item_exist == false

            cart_item = cart(Product_id = product_id, customer_id = request.session['customer'])
            cart_item.save()
            return redirect('customer:mycart')
        else :
            msg = 'Item Already In Cart'    

    return render(request, 'customertemplates/product_details.html', {'product': product_data, 'message':msg})

@auth_customer
def my_cart(request):
    cart_details = cart.objects.filter(customer = request.session['customer'])

    return render(request, 'customertemplates/my_cart.html', {'cart': cart_details})

def my_order(request):
    return render(request, 'customertemplates/my_order.html')

@auth_customer
def change_password(request):
    msg = ''
    if request.method == 'POST':
        customer = Customer.objects.get(id = request.session['customer'])

        current_pass = request.POST['curpass']
        new_pass = request.POST['newpass']
        confirm_pass = request.POST['conpass']

        if customer.password == current_pass:

            if new_pass == confirm_pass:
                customer.password = new_pass
                customer.save()
                msg = 'Password Change Successfully'
            else:
                msg = 'Password Doesnot Match' 

        else:
            msg = 'Incorrect Password'          


    return render(request, 'customertemplates/change_password.html',{'message':msg})

def profile(request):
    return render(request, 'customertemplates/profile.html')


def delete_cart(request,id):

    cart_item = cart.objects.get(Product = id, customer = request.session['customer'])

    cart_item.delete()

    return redirect('customer:mycart')


def logout(request):

    del request.session['customer']   # delete session key
    request.session.flush()   # delete data from django session table
    return redirect('common:prohome')

