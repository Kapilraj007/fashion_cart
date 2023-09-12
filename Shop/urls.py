from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name="Home"),
    path('register',views.register,name='Register'),
    path('collections',views.collections,name='Collections'),
    path('cart',views.cart_page,name='cart'),
    path('collections/<str:name>',views.collectionsview,name="collections"),
    path('collections/<str:cname>/<str:pname>',views.productdetails,name="productdetails"),
    path('login',views.login_page,name='login'),
    path('logout',views.logout_page,name='logout'),
    path('addtocart',views.add_to_cart,name='addtocart'),
    path('remove_cart/<str:cid>',views.removecart,name='remove_cart'),
   path('fav',views.fav_page,name="fav"),
    path('favviewpage',views.favviewpage,name="favviewpage"),
    path('remove_fav/<str:fid>',views.remove_fav,name="remove_fav"),






]