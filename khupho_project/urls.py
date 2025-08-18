from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView # 1. Thêm import này
# Thêm 2 dòng import này để xử lý file media
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # 2. Thêm dòng này: Chuyển hướng trang chủ đến trang /thong-bao/
    path('', RedirectView.as_view(url='/thong-bao/', permanent=True)),

    path('admin/', admin.site.urls),
    path('thong-bao/', include('thongbao.urls')),
    path('danh-ba/', include('dancu.urls')),
    path('gop-y/', include('phananh.urls')),
    path('bieu-mau/', include('bieumau.urls')),
    path('bao-cao/', include('baocao.urls')),
    path('tai-khoan/', include('django.contrib.auth.urls')),
]

# Dòng này giữ nguyên
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)