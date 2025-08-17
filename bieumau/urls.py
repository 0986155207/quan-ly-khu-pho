from django.urls import path
from . import views

urlpatterns = [
    path('', views.danh_sach_bieu_mau, name='danh_sach_bieu_mau'),
]