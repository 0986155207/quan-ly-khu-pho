from django.urls import path
from . import views

urlpatterns = [
    # Đường dẫn cho trang tìm kiếm/danh sách hộ dân mặc định
    path('', views.danh_ba, name='danh_ba_dancu'),
    
    # Đường dẫn cho trang danh sách tất cả nhân khẩu (ĐÃ SỬA LỖI)
    path('nhan-khau/', views.danh_sach_nhan_khau, name='danh_sach_nhan_khau'),

    # Đường dẫn cho trang hiển thị kết quả tìm kiếm
    path('ket-qua/', views.ket_qua_tim_kiem, name='ket_qua_tim_kiem'),
    path('ho-dan/<int:hodan_id>/', views.chi_tiet_ho_dan, name='chi_tiet_ho_dan'),
]