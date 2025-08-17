from django.shortcuts import render
from dancu.models import HoDan, NhanKhau
from django.db.models import Count
import json

def dashboard_view(request):
    # 1. Đếm tổng số
    tong_ho_dan = HoDan.objects.count()
    tong_nhan_khau = NhanKhau.objects.count()

    # 2. Thống kê giới tính
    gioi_tinh_data = NhanKhau.objects.values('gioi_tinh').annotate(so_luong=Count('gioi_tinh'))
    gioi_tinh_labels = [item['gioi_tinh'] for item in gioi_tinh_data]
    gioi_tinh_counts = [item['so_luong'] for item in gioi_tinh_data]

    # 3. Thống kê tình trạng cư trú
    tinh_trang_data = NhanKhau.objects.values('tinh_trang').annotate(so_luong=Count('tinh_trang'))
    tinh_trang_labels = []
    for item in tinh_trang_data:
        for key, value in NhanKhau.TINH_TRANG_CHOICES:
            if key == item['tinh_trang']:
                tinh_trang_labels.append(value)
                break
    tinh_trang_counts = [item['so_luong'] for item in tinh_trang_data]

    # 4. --- THỐNG KÊ MỚI: TÌNH TRẠNG HỘ ---
    tinh_trang_ho_data = HoDan.objects.values('tinh_trang_ho').annotate(so_luong=Count('tinh_trang_ho'))
    tinh_trang_ho_labels = []
    for item in tinh_trang_ho_data:
        for key, value in HoDan.TINH_TRANG_HO_CHOICES:
            if key == item['tinh_trang_ho']:
                tinh_trang_ho_labels.append(value)
                break
    tinh_trang_ho_counts = [item['so_luong'] for item in tinh_trang_ho_data]
    # -----------------------------------------

    context = {
        'tong_ho_dan': tong_ho_dan,
        'tong_nhan_khau': tong_nhan_khau,
        'gioi_tinh_labels': json.dumps(gioi_tinh_labels),
        'gioi_tinh_counts': json.dumps(gioi_tinh_counts),
        'tinh_trang_labels': json.dumps(tinh_trang_labels),
        'tinh_trang_counts': json.dumps(tinh_trang_counts),
        # Gửi dữ liệu mới sang template
        'tinh_trang_ho_labels': json.dumps(tinh_trang_ho_labels),
        'tinh_trang_ho_counts': json.dumps(tinh_trang_ho_counts),
    }
    return render(request, 'baocao/dashboard.html', context)