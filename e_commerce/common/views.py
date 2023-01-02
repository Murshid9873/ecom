from django.shortcuts import render,redirect
from.models import Customer, Seller
import random
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from .decorator import auth_customer

# Create your views here.

def customer_login(request):
    msg = ''
    if request.method == 'POST':
        username = request.POST['user_name']
        c_password = request.POST['password']

        try:
            customer = Customer.objects.get(email = username, password = c_password )
            request.session['customer'] = customer.id
            return redirect('customer:cushome')
        except :
            msg = 'incorrect username or password'

    return render(request, 'commontemplates/customer_login.html',{'message':msg})


def customer_reg(request):
    if request.method == 'POST' :   # when submit button clicked
        c_name = request.POST['Name']   # to get textbox data
        c_email = request.POST['email']
        c_phone = request.POST['phone']
        c_gender = request.POST['gender']
        c_address = request.POST['address']
        c_password = request.POST['password']

        # in ORM, if we want to insert a date in table
        # 1.create an object of model class, here model class is Customer

        new_customer = Customer(Customer_name = c_name, email = c_email, phone = c_phone, gender = c_gender,
        address = c_address, password = c_password)
        #call save() method
        new_customer.save()     

    return render(request, 'commontemplates/customer_reg.html')

@auth_customer
def project_home1(request):
    return render(request, 'commontemplates/project_home1.html')


def seller_login(request):
    msg = ''
    if request.method == 'POST' :
        s_name = request.POST['username']
        s_password = request.POST['password']

      # when we use get() to fetch data, we must use try except
      # if the data is not found in the table, exception will be raised

        try:
            seller = Seller.objects.get(user_name = s_name, password = s_password)
            request.session['seller'] = seller.id
            return redirect('reseller:rehome')
        except:
            msg = 'incorrect username & password'   
        
    return render(request, 'commontemplates/seller_login.html',{'message':msg})


def seller_reg(request):
    if request.method == 'POST' :
        s_name = request.POST['seller_name']
        s_email = request.POST['email']
        s_phone = request.POST['phone']
        s_cname = request.POST['company_name']
        s_hname = request.POST['holder_name']
        s_ifsc = request.POST['ifsc']
        s_branch = request.POST['branch']
        s_accno = request.POST['acc_no']
        s_photo = request.FILES["imgg"]

        user_name = random.randint(1111,9999)
        password = 'sel-' + str(user_name) + s_cname # result = sel-5451-john
        new_seller = Seller(seller_name = s_name, email = s_email, phone = s_phone, 
        company_name = s_cname, acc_holder_name = s_hname, ifsc = s_ifsc, branch = s_branch, acc_no = s_accno,
        upload = s_photo, password = password, user_name = user_name)

        new_seller.save()

        message = 'Hi your user name is' + str(user_name) + 'and password is ' + password

        # send_mail function used to send mail through our application
        # 1st arguement -> subject
        # 2st arguement -> message
        # 3st arguement -> from email
        # 4st arguement -> recipent list , here recipent list should be in an array format


        send_mail('username and password',  
        message,
        settings.EMAIL_HOST_USER,
        [s_email])
    

    return render(request, 'commontemplates/seller_reg.html')


def check_email(request):
    email = request.POST['email']

    exist = Customer.objects.filter(email = email).exists()

    return JsonResponse({'status' : exist})   