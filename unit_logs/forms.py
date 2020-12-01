from django import forms

from .models import Winx, Enable, Arkle, Denman, Kauto, Frankel

class WinxForm(forms.ModelForm):
    class Meta:
        model = Winx
        fields = ['number', 'status']

class EnableForm(forms.ModelForm):
    class Meta:
        model = Enable
        fields = ['number', 'status']

class ArkleForm(forms.ModelForm):
    class Meta:
        model = Arkle
        fields = ['number', 'status']

class DenmanForm(forms.ModelForm):
    class Meta:
        model = Denman
        fields = ['number', 'status']

class KautoForm(forms.ModelForm):
    class Meta:
        model = Kauto
        fields = ['number', 'status']

class FrankelForm(forms.ModelForm):
    class Meta:
        model = Frankel
        fields = ['number', 'status']
