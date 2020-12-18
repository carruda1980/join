
#coding=utf-8
from django import forms

from join.core.models import UserLocation


class UserLocationForm(forms.ModelForm):
    nome = forms.CharField(max_length=255)
    latitude = forms.CharField(max_length=255)
    longitude = forms.CharField(max_length=255)
    data_expiracao = forms.DateField(required=False, label='Data de expiração')

    class Meta:
        model = UserLocation
        fields = ['nome', 'latitude', 'longitude', 'data_expiracao']