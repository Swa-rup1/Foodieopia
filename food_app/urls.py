
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

# from .views import HomePage, SignupPage,LoginPage, LogoutPage,  

urlpatterns = [
     
    
    # path('Home/',views.HomePage,name='home'),
    path('Signup/',views.SignupPage,name='signup'),
     
    path('',views.LoginPage,name='login'),
    path('home/',views.HomePage,name='home'),
     path('home/logout/', views.user_logout, name='user_logout'),
     path('home/shop/',views.shop,name='shop'),
     path('home/fastvariety/',views.fastvariety,name='fastvariety'),
     path('home/shop/about',views.about,name='about'),
     path('home/shop/restaurant',views.about,name='restaurant'),
    #  path('place_order/', views.place_order, name='place_order'),
    # Adding Cart Urls
         path('home/shop/cart',views.view_cart,name='cart'),
         path('home/shop/product_details/<int:id>/',views.product_details,name="product-details"),
        path('home/shop/add_to_cart/<int:product_id>/<int:item_id>/<int:item_quantity>/<int:price>/',views.add_to_cart),
        path('home/shop/delete_cart/<int:cart_id>',views.delete_cart),

]
# ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    