from django.urls import path
from . import views

app_name="ecom_admin"
urlpatterns=[
    path('approve_seller',views.approve_seller),
    path('home',views.home),
    path('view_customer',views.view_customer),
    path('view_seller',views.view_seller),
]