from django.urls import path
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
]
