from django.db import models

class BieuMau(models.Model):
    ten_bieu_mau = models.CharField("Tên biểu mẫu", max_length=255)
    mo_ta = models.TextField("Mô tả ngắn", blank=True, null=True)
    file_dinh_kem = models.FileField("File đính kèm", upload_to='uploads/bieumau/')
    ngay_dang = models.DateTimeField("Ngày đăng", auto_now_add=True)

    class Meta:
        verbose_name = "Biểu mẫu"
        verbose_name_plural = "Quản lý Biểu mẫu"
        ordering = ['-ngay_dang'] # Sắp xếp theo ngày đăng mới nhất

    def __str__(self):
        return self.ten_bieu_mau