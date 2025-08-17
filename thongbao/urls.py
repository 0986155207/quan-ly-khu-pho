from django.urls import path
from . import views # Import file views.py từ cùng thư mục

urlpatterns = [
    # Dòng này định nghĩa đường dẫn cho trang danh sách thông báo
    # và gọi hàm `danh_sach_thong_bao` từ file views.py để xử lý
    path('', views.danh_sach_thong_bao, name='ds_thongbao'),
]