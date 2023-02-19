"""reviews_project URL Configuration

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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

from review_app.views import index_page, CountryViewSet, DeveloperViewSet, CarViewSet, CommentViewSet, \
    GenerateExcelView, ApiIndexPage
from rest_framework import routers





router = routers.SimpleRouter()
router.register(r'countries', CountryViewSet)
router.register(r'developers', DeveloperViewSet)
router.register(r'cars', CarViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page),
    path('api/', include(router.urls)),
    path('api/', ApiIndexPage),
    path('api/export', GenerateExcelView.as_view()),
    re_path(r'^api/auth/', include('djoser.urls')),
    re_path(r'^api/auth/', include('djoser.urls.authtoken')),
]




