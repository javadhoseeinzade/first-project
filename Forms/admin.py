from django.contrib import admin
from .models import UploadFile, info

admin.site.register(info)
admin.site.register(UploadFile)
