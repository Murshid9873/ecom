from django.urls import path
from . import views

app_name="reseller"
urlpatterns=[
    path('add_product',views.add_product,name='addpro'),
    path('change_password',views.change_password,name='chngpass'),
    path('home',views.home,name='rehome'),
    path('order_history',views.order_history,name='ordrhstry'),
    path('product_catalouge',views.product_catalouge,name='procata'),
    path('profile',views.profile,name='profile'),
    path('recent_order',views.recent_order,name='recntordr'),
    path('update_stock',views.update_stock,name='upstck'),
]