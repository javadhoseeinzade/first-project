from dataclasses import field
from django import forms
from django.forms import ModelForm
from .models import UploadFile, info, darmanjo_form

class infoss(ModelForm):
    class Meta:
        model = UploadFile
        fields = "__all__"

class darmanjo_formss(ModelForm):
    class Meta:
        model = darmanjo_form
        fields = ['talk_about','rel_info']