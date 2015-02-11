__author__ = 'diego'

from django import forms
from launcher.models import InterestedUser
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

class JoinForm(forms.ModelForm):
    # this is the only field that is actually filled by the user
    email = forms.EmailField(max_length=128, help_text="Introduce la cuenta de gmail que tienes asociada a tu"
                                                       "dispositivo Android",
                             widget=forms.EmailInput(attrs={'class': "w-input email_input",
                                                            'placeholder': 'Tu email de Google'}),
                             required=True, validators=[RegexValidator(regex='^([a-zA-Z0-9_\.\-])+\@(gmail.com)+$',
                                                                       message="La dirección de email no es válida",
                                                                       code="invalid_gmail_address")])
    print("atributos {0}".format(email.widget.attrs['class']))

    # this other fields will have the same value and go hidden in the form
    name = forms.CharField(widget=forms.HiddenInput(), initial="(not specified)")
    subject = forms.CharField(widget=forms.HiddenInput(), initial="(no subject)")
    via = forms.CharField(widget=forms.HiddenInput(), initial="Join")
    content = forms.CharField(widget=forms.HiddenInput(), initial="no content")


    # TODO: tengo que comprobar que sea un error de gmail, sino lanzar un alert
    # Lanzo errores si no valida con respecto al RegexValidator y también si la dirección ya existe en la BBDD.
    def clean_email(self):
        email = self.cleaned_data.get('email')

        try:
            beta_tester = InterestedUser.objects.get(email=email)
        # Si el email no existiese entonces salimos del clean_email y devolvemos el valor (aunque no se haya modificado)
        except InterestedUser.DoesNotExist:
            return email
        # Si el email ya existía sacamos un error de Validación:
        raise forms.ValidationError("Ya estabas anotado como Beta Tester, introduce un email diferente!")


    class Meta:
        model = InterestedUser
        fields = ('email', 'name', 'subject', 'via', 'content',)