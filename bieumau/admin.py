from django.contrib import admin
from .models import BieuMau

class BieuMauAdmin(admin.ModelAdmin):
    list_display = ('ten_bieu_mau', 'ngay_dang')
    search_fields = ('ten_bieu_mau', 'mo_ta')

admin.site.register(BieuMau, BieuMauAdmin)
