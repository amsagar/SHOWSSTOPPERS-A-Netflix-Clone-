"""SS URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from MyApp import views as AppV
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', AppV.index),
    path('loggedout/', AppV.log_out),
    path('home/', AppV.movieList),
    path('dashbord/', AppV.dash),
    path('accounts/', include('allauth.urls')),
    path('detail/<str:name>', AppV.details),
    path('<str:title>/play', AppV.play_view),
    path('admin/', admin.site.urls),
    path('search/', AppV.ser),
    path('res/', AppV.res),
    path('latest/', AppV.lat_view)
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
