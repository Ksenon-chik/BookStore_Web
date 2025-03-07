from django.contrib import admin
from django.urls import path, include
from books import views  # Импортируем views, чтобы использовать index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Главная страница
    path('books/', include('books.urls')),  # Подключаем маршруты книг
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
]
