from django.contrib import admin
from .models import PhanAnh

# Lớp này giúp chúng ta tùy chỉnh cách hiển thị của model PhanAnh trong trang Admin
class PhanAnhAdmin(admin.ModelAdmin):
    # Hiển thị các cột này trong danh sách các phản ánh
    list_display = ('ho_ten', 'so_dien_thoai', 'tinh_trang', 'ngay_gui')

    # Thêm một bộ lọc ở bên tay phải, cho phép lọc theo tình trạng và ngày gửi
    list_filter = ('tinh_trang', 'ngay_gui')

    # Thêm một ô tìm kiếm, cho phép tìm theo họ tên và nội dung
    search_fields = ('ho_ten', 'noi_dung')

# Đăng ký model PhanAnh với lớp tùy chỉnh PhanAnhAdmin ở trên
admin.site.register(PhanAnh, PhanAnhAdmin)
