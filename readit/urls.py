"""readit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
import debug_toolbar

from django.urls import re_path, path, include
from django.contrib import admin

from books.views import AuthorDetail, AuthorList, BookDetail, list_books

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', list_books, name="books"),
    path('__debug__/', include('debug_toolbar.urls')),
    re_path(r'^authors/$', AuthorList.as_view(), name='authors'),
    re_path(r'^books/(?P<pk>[-\w]+)/$', BookDetail.as_view(), name='book-detail'),
    re_path(r'^authors/(?P<pk>[-\w]+)/$', AuthorDetail.as_view(), name='author-detail'),
]
