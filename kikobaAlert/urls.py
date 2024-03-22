from django.urls import path
from . import views

#Here is where all endpoints for kikobaAlert Application are located
urlpatterns = [
    
    path('',views.about_view,name='about'),
    path('manager/dashboard/',views.admin_dashboard_view,name='admin'),
    path('customer/dashboard/',views.customer_dashboard_view,name='customer'),
    path('login/',views.login_view,name='login'),
    path('register/',views.register_view,name='register'),
    
]
