__author__ = 'diego'

from django import forms
from launcher.models import InterestedUser
from django.core import validators
from nocaptcha_recaptcha.fields import NoReCaptchaField


class ContactForm(forms.ModelForm):

    def __init__(self, needs_captcha, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not needs_captcha:
            # del self.fields['captcha']
            print("captcha won't be included")
        else:
            print("captcha will be included")

    email = forms.EmailField(max_length=128, help_text="Tu email", widget=forms.EmailInput(
                             attrs={'class': "w-input email_field email_input", 'placeholder': 'Tu email'}),
                             required=True)

    captcha = NoReCaptchaField(required=True, gtag_attrs={'data-theme': 'light'})

    name = forms.CharField(max_length=128, help_text="Tu nombre", required=True, widget=forms.TextInput(
                           attrs={'class': "w-input name_field email_input", 'placeholder': 'Tu nombre'}))

    subject = forms.CharField(max_length=256, help_text="Asunto", required=False,
                              widget=forms.TextInput(attrs={'class': "w-input asunto_field email_input",
                                                            'placeholder': 'Asunto'}))

    content = forms.CharField(max_length=1000, help_text="Escribe tu mensaje", required=True,
                              widget=forms.Textarea(
                                  attrs={'class': "w-input text_field", 'style': "height: 208px;", 'placeholder': 'Escribe aquí tu mensaje...'}))

    via = forms.CharField(required=False, widget=forms.HiddenInput(), initial="Escribenos")

    def clean(self):
        cleaned_data = self.cleaned_data

        cleaned_data['via'] = "Escribenos"

        if 'subject' not in cleaned_data.keys() or len(cleaned_data.get('subject')) == 0:
            subject = "(Sin asunto)"
            cleaned_data['subject'] = subject
        return cleaned_data

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            validators.validate_email(email)
        except forms.ValidationError:
            print("el email introducido no es válido")
            raise forms.ValidationError("Por favor introduce una dirección de email válida", code="email_malformed")
        # Siempre hay que devolver el campo que se está limpiando, por si se ha modificado en la función
        return email

    class Meta:
        model = InterestedUser
        fields = ('email', 'name', 'subject', 'via', 'content',)


class JoinForm(forms.ModelForm):

    def __init__(self, needs_captcha, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not needs_captcha:
            del self.fields['captcha']
            print("captcha won't be included")
        else:
            print("captcha will be included")

    # this is the only field that is actually filled by the user
    email = forms.EmailField(max_length=128, help_text="Introduce la cuenta de gmail que tienes asociada a tu"
                                                       " dispositivo Android",
                             widget=forms.EmailInput(attrs={'class': "w-input email_input",
                                                            'placeholder': 'Tu cuenta de Google'}),
                             required=True)

    captcha = NoReCaptchaField(required=True, gtag_attrs={'data-theme': 'light'})
    name = forms.CharField(required=False, widget=forms.HiddenInput(), initial="(not specified)")
    subject = forms.CharField(required=False, widget=forms.HiddenInput(), initial="(no subject)")
    via = forms.CharField(required=False, widget=forms.HiddenInput(), initial="Join")
    content = forms.CharField(required=False, widget=forms.HiddenInput(), initial="no content")

    # Lanzo errores si no valida bien el email y también si la dirección ya existe en la BBDD.

    def clean(self):
        cleaned_data = self.cleaned_data
        cleaned_data['name'] = "(not specified)"
        cleaned_data['subject'] = "(not specified)"
        cleaned_data['via'] = "Join"
        cleaned_data['content'] = "(not specified)"
        return cleaned_data

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            validators.validate_email(email)
        except forms.ValidationError:
            print("el email introducido no es válido")
            raise forms.ValidationError("Por favor introduce una dirección de email válida", code="email_malformed")
        try:
            user = InterestedUser.objects.get(email=email)
        # Si el email no existiese entonces salimos del clean_email y devolvemos el valor (aunque no se haya modificado)
        except InterestedUser.DoesNotExist:
            # no tenemos que hacer nada, es lo esperado
            print("el email es válido y se va a añadir el usuario a la BBDD!")
            pass
        else:
            if user.via == "Join":
                # Si el email ya existía y provenía del formulario Join sacamos un error de Validación:
                print("el email ya existía por lo que se genera un error")
                raise forms.ValidationError("Ya estabas anotado como Beta Tester, introduce un email diferente!",
                                            code="user_exists")
        # Siempre hay que devolver el campo que se está limpiando, por si se ha modificado en la función
        return email

    class Meta:
        model = InterestedUser
        fields = ('email', 'name', 'subject', 'via', 'content',)