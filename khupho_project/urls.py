from django.contrib import admin
from django.urls import path, include # 1. Sửa dòng này để thêm 'include'
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('thong-bao/', include('thongbao.urls')), # 2. Thêm dòng này
    path('danh-ba/', include('dancu.urls')), # Thêm dòng này
    path('gop-y/', include('phananh.urls')),
    path('bieu-mau/', include('bieumau.urls')), # Thêm dòng này
    path('bao-cao/', include('baocao.urls')), # Thêm dòng này
    path('tai-khoan/', include('django.contrib.auth.urls')),
]
# Thêm dòng này vào cuối file để server có thể hiển thị ảnh bạn đã upload
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)