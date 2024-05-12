from django import forms
from .models import Duo, Solo, Famille, CreditCardHolder


class SoloForm(forms.ModelForm):
    class Meta:
        model = Solo
        fields = ["first_name", "last_name"]

    def __init__(self, *args, **kwargs):
        super(SoloForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Prénom'
        self.fields['first_name'].label = ''

        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Nom'
        self.fields['last_name'].label = ''


class DuoForm(forms.ModelForm):
    class Meta:
        model = Duo
        fields = ["first_name", "last_name"]

    def __init__(self, *args, **kwargs):
        super(DuoForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Prénom'
        self.fields['first_name'].label = ''

        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Nom'
        self.fields['last_name'].label = ''


class FamilleForm(forms.ModelForm):
    class Meta:
        model = Famille
        fields = ["first_name", "last_name"]

    def __init__(self, *args, **kwargs):
        super(FamilleForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Prénom'
        self.fields['first_name'].label = ''

        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Nom'
        self.fields['last_name'].label = ''


class CreditCardHolderForm(forms.ModelForm):
    class Meta:
        model = CreditCardHolder
        fields = ["holder_name", "card_number", "card_validation_code", "card_validity"]
        widgets={
            "card_validity": forms.SelectDateWidget(years=range(2020, 2050), attrs=({'style': 'width: 18%; display: inline-block;'}))
        }

    def __init__(self, *args, **kwargs):
        super(CreditCardHolderForm, self).__init__(*args, **kwargs)

        self.fields['holder_name'].widget.attrs['class'] = 'form-control'
        self.fields['holder_name'].widget.attrs['placeholder'] = 'Nom du titulaire de la carte'
        self.fields['holder_name'].label = ''

        self.fields['card_number'].widget.attrs['class'] = 'form-control'
        self.fields['card_number'].widget.attrs['placeholder'] = 'Numéro de la carte'
        self.fields['card_number'].label = ''

        self.fields['card_validation_code'].widget.attrs['class'] = 'form-control'
        self.fields['card_validation_code'].widget.attrs['placeholder'] = 'Cryptogramme'
        self.fields['card_validation_code'].label = ''

        self.fields['card_validity'].widget.attrs['class'] = 'form-control'
        self.fields['card_validity'].widget.attrs['placeholder'] = 'Date expiration'
        self.fields['card_validity'].label = ''
