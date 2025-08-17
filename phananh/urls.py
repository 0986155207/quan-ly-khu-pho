from django.urls import path
from . import views

urlpatterns = [
    path('', views.form_phan_anh, name='form_phan_anh'),
    path('cam-on/', views.trang_cam_on, name='trang_cam_on'),
]