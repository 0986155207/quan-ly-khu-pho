from django.db import models

# Create your models here.

class HoDan(models.Model):
    # --- PHẦN MỚI ĐƯỢC THÊM VÀO ---
    TINH_TRANG_HO_CHOICES = [
        ('binh_thuong', 'Bình thường'),
        ('kinh_doanh', 'Hộ kinh doanh'),
        ('cho_thue', 'Hộ cho thuê'),
        ('ho_ngheo', 'Hộ nghèo'),
        ('can_ngheo', 'Hộ cận nghèo'),
        ('chinh_sach', 'Gia đình chính sách'),
    ]
    # --------------------------------

    chu_ho = models.ForeignKey(
        'NhanKhau', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='ho_dan_la_chu_ho',
        verbose_name="Chủ hộ"
    )
    so_nha = models.CharField("Số nhà", max_length=50)
    khu_vuc = models.CharField("Khu vực (Hẻm, Tổ...)", max_length=100)
    dia_chi_cu_the = models.CharField("Địa chỉ cụ thể", max_length=255, blank=True, null=True)
    so_dien_thoai = models.CharField("Số điện thoại", max_length=15, blank=True, null=True)
    
    # --- DÒNG ĐƯỢC CẬP NHẬT ---
    tinh_trang_ho = models.CharField(
        "Tình trạng hộ", 
        max_length=20, 
        choices=TINH_TRANG_HO_CHOICES, 
        default='binh_thuong'
    )
    # ---------------------------

    class Meta:
        verbose_name = "Hộ dân"
        verbose_name_plural = "Quản lý Hộ dân"

    def __str__(self):
        if self.chu_ho:
            return f"Hộ ông/bà {self.chu_ho.ho_va_ten} - Số nhà {self.so_nha}, {self.khu_vuc}"
        return f"Hộ chưa có chủ hộ - Số nhà {self.so_nha}, {self.khu_vuc}"


class NhanKhau(models.Model):
    GIOI_TINH_CHOICES = [
        ('Nam', 'Nam'),
        ('Nữ', 'Nữ'),
        ('Khác', 'Khác'),
    ]
    
    TINH_TRANG_CHOICES = [
        ('thuong_tru', 'Thường trú'),
        ('tam_tru', 'Tạm trú'),
        ('vang_mat', 'Vắng mặt tại địa phương'),
        ('da_mat', 'Đã mất'),
    ]

    QUAN_HE_CHOICES = [
        ('chu_ho', 'Chủ hộ'),
        ('vo', 'Vợ'),
        ('chong', 'Chồng'),
        ('con', 'Con'),
        ('bo', 'Bố'),
        ('me', 'Mẹ'),
        ('ong', 'Ông'),
        ('ba', 'Bà'),
        ('chau', 'Cháu'),
        ('khac', 'Khác'),
    ]

    ho_dan = models.ForeignKey(HoDan, on_delete=models.CASCADE, verbose_name="Thuộc hộ dân")
    ho_va_ten = models.CharField("Họ và tên", max_length=150)
    
    quan_he_chu_ho = models.CharField(
        "Quan hệ với chủ hộ",
        max_length=20,
        choices=QUAN_HE_CHOICES,
        default='chu_ho'
    )

    ngay_sinh = models.DateField("Ngày sinh", blank=True, null=True)
    gioi_tinh = models.CharField("Giới tính", max_length=5, choices=GIOI_TINH_CHOICES)
    
    tinh_trang = models.CharField(
        "Tình trạng", 
        max_length=20, 
        choices=TINH_TRANG_CHOICES, 
        default='thuong_tru'
    )
    
    so_cccd = models.CharField("Số CCCD/CMND", max_length=12, unique=True, blank=True, null=True)
    cong_viec_hien_nay = models.CharField("Công việc hiện nay", max_length=255, blank=True, null=True)
    noi_o_hien_nay = models.CharField("Nơi ở hiện nay", max_length=255, blank=True, null=True)
    
    class Meta:
        verbose_name = "Nhân khẩu"
        verbose_name_plural = "Quản lý Nhân khẩu"

    def __str__(self):
        return self.ho_va_ten