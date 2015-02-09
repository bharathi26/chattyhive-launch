__author__ = 'diego'

from django import forms
from launcher.models import InterestedUser


class JoinForm(forms.ModelForm):
    #this is the only field that is actually filled by the user
    email = forms.EmailField(max_length=128, widget=forms.EmailInput(attrs={'class': "w-input email_input",
                                                                            'placeholder': 'Tu email de Google'}))
    print("atributos {0}".format(email.widget.attrs['class']))

    #this other fields will have the same value and go hidden in the form
    name = forms.CharField(widget=forms.HiddenInput(), initial="(not specified)")
    subject = forms.CharField(widget=forms.HiddenInput(), initial="(no subject)")
    via = forms.CharField(widget=forms.HiddenInput(), initial="Join")
    content = forms.CharField(widget=forms.HiddenInput(), initial="no content")


    # #TODO: tengo que comprobar que sea un error de gmail, sino lanzar un alert
    # def clean(self):
    #     cleaned_data = self.cleaned_data
    #     email = cleaned_data.get('url')

    class Meta:
        model = InterestedUser
        fields = ('email', 'name', 'subject', 'via', 'content',)