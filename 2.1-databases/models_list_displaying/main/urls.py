"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from books.views import books_view, book_view

urlpatterns = [
    path('books/', books_view, name='books'),
    path('books/voina-i-mir/', book_view, name='voina-i-mir'),
    path('books/1984/', book_view, name='1984'),
    path('books/skotnyi-dvor/', book_view, name='skotnyi-dvor'),
    path('books/v-pamiat-o-proshlom-zemli/', book_view, name='v-pamiat-o-proshlom-zemli'),
    path('admin/', admin.site.urls),
]
