from django.db import models
from django.contrib.auth.models import User # Dòng này để liên kết với bảng người dùng có sẵn của Django

# Create your models here.

class ThongBao(models.Model):
    tieu_de = models.CharField("Tiêu đề", max_length=255)
    noi_dung = models.TextField("Nội dung")
    ngay_dang = models.DateTimeField("Ngày đăng", auto_now_add=True)
    nguoi_dang = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Người đăng")

    class Meta:
        verbose_name = "Thông báo"
        verbose_name_plural = "Các thông báo"

    def __str__(self):
        return self.tieu_de