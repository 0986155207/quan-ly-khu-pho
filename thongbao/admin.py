from django.contrib import admin
from .models import ThongBao

# Lớp này giúp tùy chỉnh hiển thị cho model ThongBao
class ThongBaoAdmin(admin.ModelAdmin):
    # Hiển thị các cột này trong danh sách
    list_display = ('tieu_de', 'nguoi_dang', 'ngay_dang')

    # Thêm dòng quan trọng này để bật phân trang
    list_per_page = 5 # Hiển thị 5 thông báo mỗi trang trong Admin

# Đăng ký model ThongBao với lớp tùy chỉnh ở trên
admin.site.register(ThongBao, ThongBaoAdmin)
