from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView
from .views import (
    index,
    register_view,
    login_view,
    logout_view,
    profile_view,
)

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
    path('profile/', profile_view, name='profile'),

    path('books/', views.book_list, name='book_list'),
    path('books/create/', views.book_create, name='book_create'),
    path('books/<int:pk>/update/', views.book_update, name='book_update'),
    path('books/<int:pk>/delete/', views.book_delete, name='book_delete'),

    path('add_to_cart/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart'),
    path('remove_from_cart/<int:cart_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('orders/', views.order_list, name='order_list'),
    path('checkout/', views.checkout, name='checkout'),

    path('captcha/', include('captcha.urls')),

    path("ajax/check_username/", views.check_username, name='check_username'),
    path('ajax/check_email/', views.check_email, name='check_email'),
]
