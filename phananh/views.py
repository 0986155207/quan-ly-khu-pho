# --- Đây là phiên bản cuối cùng, tinh gọn nhất ---

from django.shortcuts import render, redirect
from .models import PhanAnh

def form_phan_anh(request):
    if request.method == 'POST':
        # Lấy dữ liệu từ form
        ho_ten = request.POST.get('ho_ten')
        sdt = request.POST.get('so_dien_thoai')
        noi_dung = request.POST.get('noi_dung')
        hinh_anh = request.FILES.get('hinh_anh')

        # Chỉ lưu dữ liệu vào database, không thực hiện gửi thông báo
        PhanAnh.objects.create(
            ho_ten=ho_ten,
            so_dien_thoai=sdt,
            noi_dung=noi_dung,
            hinh_anh=hinh_anh,
        )

        # Chuyển hướng đến trang cảm ơn
        return redirect('trang_cam_on') 
    
    return render(request, 'phananh/form.html')

def trang_cam_on(request):
    # View đơn giản để hiển thị trang cảm ơn
    return render(request, 'phananh/cam_on.html')