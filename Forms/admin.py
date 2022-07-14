from django.contrib import admin
from .models import UploadFile, info,darmangar ,darmanjo_form,Choice_Model

admin.site.register(info)
admin.site.register(UploadFile)
admin.site.register(darmangar)
class darmanjoform(admin.ModelAdmin):
    list_display = ['talk_about', 'rel_info', 'information']
admin.site.register(darmanjo_form, darmanjoform)
admin.site.register(Choice_Model)
