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
from django.contrib import admin
from django.urls import path, include

from review_app.views import index_page, CountryViewSet, DeveloperViewSet, CarViewSet, CommentViewSet, \
    GenerateExcelView, CSVviewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'country', CountryViewSet)
router.register(r'developer', DeveloperViewSet)
router.register(r'car', CarViewSet)
router.register(r'comment', CommentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page),
    path('api/', include(router.urls)),
    path('api/export', GenerateExcelView.as_view(), name='export'),
    path('api/csv', CSVviewSet.as_view()),
]





