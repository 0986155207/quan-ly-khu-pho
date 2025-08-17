from django.contrib import admin
from .models import HoDan, NhanKhau

# --- BỔ SUNG ĐOẠN MÃ TÙY CHỈNH NÀY VÀO ĐẦU FILE ---
admin.site.site_header = "TRANG QUẢN TRỊ KHU PHỐ 25"
admin.site.site_title = "Admin KP25"
admin.site.index_title = "Chào mừng đến với trang quản trị Khu phố 25"
# ---------------------------------------------------

# Lớp tùy chỉnh cho Hộ Dân
class HoDanAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'khu_vuc', 'so_dien_thoai', 'tinh_trang_ho')
    search_fields = ('chu_ho__ho_va_ten', 'so_nha', 'khu_vuc')
    list_filter = ('khu_vuc', 'tinh_trang_ho')
    list_per_page = 15

# Lớp tùy chỉnh cho Nhân Khẩu
class NhanKhauAdmin(admin.ModelAdmin):
    list_display = ('ho_va_ten', 'ho_dan', 'ngay_sinh', 'tinh_trang', 'quan_he_chu_ho')
    search_fields = ('ho_va_ten', 'so_cccd')
    list_filter = ('tinh_trang', 'gioi_tinh', 'ho_dan__khu_vuc')
    list_per_page = 20

# Đăng ký các model với lớp tùy chỉnh tương ứng
admin.site.register(HoDan, HoDanAdmin)
admin.site.register(NhanKhau, NhanKhauAdmin)