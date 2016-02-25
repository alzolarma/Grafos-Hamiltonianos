#encoding:utf-8
from django.forms import ModelForm
from django import forms
from principal.models import Grafo , Historial

class GrafoForm(forms.Form):
	nodes = forms.CharField(max_length=50)
    edges = forms.CharField(max_length=100)
   
