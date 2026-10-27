
from django import forms
from .models import (
    DonorScreening,
    ComponentSeparation,
    ColdStorage,
    Dispatch,
)


class DonorScreeningForm(forms.ModelForm):
    class Meta:
        model = DonorScreening
        fields = '__all__'
        widgets = {
            'screening_date': forms.DateInput(
                attrs={'type': 'date'}
            ),
        }


class ComponentSeparationForm(forms.ModelForm):
    class Meta:
        model = ComponentSeparation
        fields = '__all__'
        widgets = {
            'separation_date': forms.DateInput(
                attrs={'type': 'date'}
            ),
        }


class ColdStorageForm(forms.ModelForm):
    class Meta:
        model = ColdStorage
        fields = '__all__'
        widgets = {
            'expiry_date': forms.DateInput(
                attrs={'type': 'date'}
            ),
        }


class DispatchForm(forms.ModelForm):
    class Meta:
        model = Dispatch
        fields = '__all__'
        widgets = {
            'dispatch_date': forms.DateInput(
                attrs={'type': 'date'}
            ),
        }
