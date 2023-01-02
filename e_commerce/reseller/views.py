from django.shortcuts import render
from.models import Product , Seller



# Create your views here.

def add_product(request):

    msg = ''
    if request.method == 'POST':
        pro_name = request.POST['product_name']
        pro_description = request.POST['description']
        pro_no = request.POST['product_no']
        pro_photo = request.FILES['upload']
        pro_price = request.POST['price']
        pro_stock = request.POST['stock']

        new_product = Product(p_name = pro_name, description = pro_description, p_no = pro_no, upload = pro_photo,
        price = pro_price, stock = pro_stock, seller_id = request.session['seller'])    

        new_product.save()

        msg = 'Item added successfully'


    return render(request, 'resellertemplates/add_product.html', {'message' : msg})

def change_password(request):
    msg = ''
    if request.method == 'POST':

        current_pass = request.POST['curpass']
        new_pass = request.POST['newpass']
        confirm_pass = request.POST['conpass']

        seller = Seller.objects.get(id = request.session['seller']) 
        if seller.password == current_pass:

            if new_pass == confirm_pass:
                Seller.objects.filter(id = request.session['seller']).update(password = new_pass)
                msg = 'Password Change Successfully'
            else:
                msg = 'Password Doesnot Match' 

        else:
            msg = 'Incorrect Password'          


    return render(request, 'resellertemplates/change_password.html',{'message':msg})

def home(request):
    return render(request, 'resellertemplates/home.html')

def order_history(request):
    return render(request, 'resellertemplates/order_history.html')

def product_catalouge(request):
    seller_data = Seller.objects.get(id = request.session['seller'])
    seller_products = Product.objects.filter(seller = request.session['seller'])
   
    return render(request, 'resellertemplates/product_catalouge.html',{'products': seller_products})

def profile(request):
    return render(request, 'resellertemplates/profile.html')

def recent_order(request):
    return render(request, 'resellertemplates/recent_order.html')

def update_stock(request):
    return render(request, 'resellertemplates/update_stock.html')
