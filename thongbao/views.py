from django.shortcuts import render
from .models import ThongBao
from django.core.paginator import Paginator

def danh_sach_thong_bao(request):
    danh_sach_goc = ThongBao.objects.all().order_by('-ngay_dang')

    # --- PHẦN CODE MỚI ĐỂ SỬA LỖI ---
    # Xử lý trước dữ liệu để thêm độ trễ animation
    danh_sach_da_xu_ly = []
    for index, tb in enumerate(danh_sach_goc):
        tb.animation_delay = index * 0.1
        danh_sach_da_xu_ly.append(tb)
    # -----------------------------------

    # Phân trang trên danh sách đã xử lý
    paginator = Paginator(danh_sach_da_xu_ly, 5) # 5 thông báo mỗi trang
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj 
    }
    return render(request, 'thongbao/danh_sach.html', context)