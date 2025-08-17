from django.db import models

class PhanAnh(models.Model):
    TINH_TRANG_CHOICES = [
        ('moi', 'Mới tiếp nhận'),
        ('dang_xu_ly', 'Đang xử lý'),
        ('da_xu_ly', 'Đã xử lý'),
    ]

    ho_ten = models.CharField("Họ và tên người gửi", max_length=150)
    so_dien_thoai = models.CharField("Số điện thoại liên hệ", max_length=15)
    noi_dung = models.TextField("Vị trí sự cố hoặc nội dung góp ý")
    hinh_anh = models.ImageField("Hình ảnh sự cố", upload_to='uploads/phananh/', blank=True, null=True)
    tinh_trang = models.CharField("Tình trạng", max_length=20, choices=TINH_TRANG_CHOICES, default='moi')
    ngay_gui = models.DateTimeField("Ngày gửi", auto_now_add=True)

    class Meta:
        verbose_name = "Phản ánh"
        verbose_name_plural = "Quản lý Phản ánh"

    def __str__(self):
        return f"Phản ánh từ {self.ho_ten} - {self.ngay_gui.strftime('%d/%m/%Y')}"
