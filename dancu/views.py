from django.shortcuts import render, get_object_or_404
from .models import HoDan, NhanKhau
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required
def danh_ba(request):
    danh_sach_ho_dan = HoDan.objects.all().order_by('khu_vuc', 'so_nha')
    paginator = Paginator(danh_sach_ho_dan, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'dancu/danh_ba.html', context)

@login_required
def ket_qua_tim_kiem(request):
    query_hodan = request.GET.get('q_hodan', '')
    query_nhankhau = request.GET.get('q_nhankhau', '')

    ket_qua = None
    search_type = ''

    if query_hodan:
        search_type = 'hodan'
        ket_qua = HoDan.objects.filter(
            Q(dia_chi_cu_the__icontains=query_hodan) | 
            Q(so_nha__icontains=query_hodan) |
            Q(khu_vuc__icontains=query_hodan)
        ).distinct()

    elif query_nhankhau:
        search_type = 'nhankhau'
        ket_qua = NhanKhau.objects.filter(ho_va_ten__icontains=query_nhankhau)

    context = {
        'ket_qua': ket_qua,
        'search_type': search_type,
        'query_hodan': query_hodan,
        'query_nhankhau': query_nhankhau,
    }
    return render(request, 'dancu/ket_qua_tim_kiem.html', context)

@login_required
def danh_sach_nhan_khau(request):
    danh_sach_goc = NhanKhau.objects.all().order_by('ho_va_ten')
    paginator = Paginator(danh_sach_goc, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(request, 'dancu/danh_sach_nhan_khau.html', context)

@login_required # <-- DÒNG CÒN THIẾU LÀ Ở ĐÂY
def chi_tiet_ho_dan(request, hodan_id):
    hodan = get_object_or_404(HoDan, pk=hodan_id)
    thanh_vien_trong_ho = NhanKhau.objects.filter(ho_dan=hodan)
    context = {
        'hodan': hodan,
        'thanh_vien_trong_ho': thanh_vien_trong_ho
    }
    return render(request, 'dancu/chi_tiet_ho_dan.html', context)