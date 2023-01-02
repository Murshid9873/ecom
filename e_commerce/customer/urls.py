from django.urls import path
from . import views

app_name="customer"
urlpatterns=[
    path('home',views.home,name='cushome'),
    path('product_details/<int:pid>',views.product_details,name='prodetails'),

    path('my_cart',views.my_cart,name='mycart'),
    path('delete/<int:id>',views.delete_cart,name='del_cart'),

    path('my_order',views.my_cart,name='myorder'),
    path('change_password',views.change_password,name='chngpass'),
    path('profile',views.profile,name='profile'),

    path('logout',views.logout,name='logout'),
    
]    