from django import forms
from django.forms import ModelForm
from .models import UploadFile, info

class infoss(ModelForm):
    class Meta:
        model = UploadFile
        fields = "__all__"

