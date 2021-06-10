from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home),
    path('showcakes/<id>',views.showCake),
    path('viewDetails/<id>',views.viewDetails),
    path('signup',views.signup),
    path('login',views.login),
    path('logout',views.logout),
    path('addtocart',views.addtocart),
    path('cart',views.showcart),
]
