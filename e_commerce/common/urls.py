from django.urls import path
from . import views

app_name="common"
urlpatterns=[
    path('customer_login',views.customer_login,name='custlo'),
    path('customer_reg',views.customer_reg,name='custreg'),
    path('',views.project_home1,name='prohome'),
    path('seller_login',views.seller_login,name='sellerlog'),
    path('seller_reg',views.seller_reg,name='sellerreg'),
    path('check_email',views.check_email,name='check_email'),
]    