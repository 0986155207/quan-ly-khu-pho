from django.shortcuts import render
from .models import BieuMau

def danh_sach_bieu_mau(request):
    danh_sach = BieuMau.objects.all()
    context = {
        'danh_sach_bieu_mau': danh_sach,
    }
    return render(request, 'bieumau/danh_sach.html', context)