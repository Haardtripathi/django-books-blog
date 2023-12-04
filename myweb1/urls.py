from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('about',views.about,name="about"),
    path('blog-post/<str:pk>/',views.blogpost,name="blogpost"),
    path('blog',views.blog,name="blog"),
    path('checkout',views.checkout,name="checkout"),
    path('contact',views.contact,name="contact"),
    path('productdetails/<str:pk>/',views.productdetails,name="productdetails"),
    path('products',views.products,name="products"),
    path('terms',views.terms,name="terms"),
    path('testimonials',views.testimonials,name="testimonials"),

    path('contact1',views.Insertrecord,name="contact1")

]