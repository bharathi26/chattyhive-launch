__author__ = 'diego'

from django import forms
from launcher.models import InterestedUser
from django.core import validators
from nocaptcha_recaptcha.fields import NoReCaptchaField


class JoinForm(forms.ModelForm):
    # this is the only field that is actually filled by the user
    captcha = NoReCaptchaField(gtag_attrs={'data-theme': 'light'})
    email = forms.EmailField(max_length=128, help_text="Introduce la cuenta de gmail que tienes asociada a tu"
                                                       " dispositivo Android",
                             widget=forms.EmailInput(attrs={'class': "w-input email_input",
                                                            'placeholder': 'Tu cuenta de Google'}),
                             required=True)

    print("atributos {0}".format(email.widget.attrs['class']))

    # this other fields will have the same value and go hidden in the form
    name = forms.CharField(widget=forms.HiddenInput(), initial="(not specified)")
    subject = forms.CharField(widget=forms.HiddenInput(), initial="(no subject)")
    via = forms.CharField(widget=forms.HiddenInput(), initial="Join")
    content = forms.CharField(widget=forms.HiddenInput(), initial="no content")

    # Lanzo errores si no valida bien el email y también si la dirección ya existe en la BBDD.
    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            validators.validate_email(email)
        except forms.ValidationError:
            raise forms.ValidationError("Por faver introduce una dirección de email válida", code="email_malformed")
        try:
            InterestedUser.objects.get(email=email)
        # Si el email no existiese entonces salimos del clean_email y devolvemos el valor (aunque no se haya modificado)
        except InterestedUser.DoesNotExist:
            # no tenemos que hacer nada, es lo esperado
            print("el email es válido y se va a añadir el usuario a la BBDD!")
            pass
        else:
            # Si el email ya existía sacamos un error de Validación:
            raise forms.ValidationError("Ya estabas anotado como Beta Tester, introduce un email diferente!",
                                        code="user_exists")
        # Siempre hay que devolver el campo que se está limpiando, por si se ha modificado en la función
        return email

    class Meta:
        model = InterestedUser
        fields = ('email', 'name', 'subject', 'via', 'content',)