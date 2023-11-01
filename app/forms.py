from django import forms
from .models import *
from rest_framework import serializers
  
class StudentForm(forms.ModelForm):
  
    class Meta:
        model = arch
        fields = ['files']

# class StudentForm(serializers.ModelSerializer):
  
#     class Meta:
#         model = arch
#         fields = ['files']