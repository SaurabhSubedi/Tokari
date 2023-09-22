from django.urls import path

from . import views

urlpatterns = [
    path('',views.store,name='store'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('update_item/',views.updateItem, name='updateItem'),
    path('product_detail/<int:pk>',views.ProductDetail.as_view(),name= 'productdetail'),
    path('logout/',views.logout_view,name = 'logout'),
    path('login/',views.login_view,name = 'login'),
    path('signup/',views.signup, name = 'signup'),
    path('about/',views.about_view,name='aboutus'),
    path('contact/',views.contact_view,name = 'contact'),
]
