from django.core.mail import send_mail

# Create your views here.
from django.shortcuts import render
from .forms import JoinForm, ContactForm
from django.conf import settings


def about(request):
    context_dict = {'alert': 'nothing'}

    #Inicializamos correctamente la necesidad de captcha
    if 'attempt_about' in request.session.keys() and request.session['attempt_about'] == 0:
        needs_captcha = True
    else:
        needs_captcha = False

    if request.method == 'POST':
        # Getting info from the POST
        form = ContactForm(needs_captcha, request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            # We save what we receive in the form and that is already associated with InterestedUser model
            form.save(commit=True)
            send_mail(form.cleaned_data['subject'] + ' de ' + form.cleaned_data['name'], form.cleaned_data['content'],
                      form.cleaned_data['email'], ['chattyhive@gmail.com'],
                      fail_silently=False)
            print("email enviado")

            # We only want to show captcha if it is the third time an email is registered
            if 'attempt_about' in request.session.keys():
                if request.session['attempt_about'] == 3:
                    request.session['attempt_about'] = 0
                    needs_captcha = True
                else:
                    request.session['attempt_about'] += 1
            else:
                request.session['attempt_about'] = 1
                needs_captcha = False

            context_dict['alert'] = "successful"

        else:
            # se procesan los errores
            errors = form.errors.as_data()
            if 'captcha' in errors:
                context_dict['alert'] = "needs_captcha"
            print(errors)

    form = ContactForm(needs_captcha)
    context_dict['form'] = form
    return render(request, "about.html", context_dict)


def home(request):
    context_dict = {'alert': 'nothing'}

    #Inicializamos correctamente la necesidad de captcha
    if 'attempt_join' in request.session.keys() and request.session['attempt_join'] == 0:
        needs_captcha = True
    else:
        needs_captcha = False

    if request.method == 'POST':
        # Getting info from the POST
        form = JoinForm(needs_captcha, request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            # We save what we receive in the form and that is already associated with InterestedUser model
            form.save(commit=True)

            if settings.ACTIVAR_EMAILS_EN_JOIN:
                send_mail('Nueva suscrpcion a chattyhive Beta Launch!',
                          'Un nuevo usuario se ha suscrito a la Beta su email es: ' + form.cleaned_data['email'],
                          form.cleaned_data['email'], ['chattyhive@gmail.com'], fail_silently=False)
                print("email enviado")
            # We only want to show captcha if it is the third time an email is registered
            if 'attempt_join' in request.session.keys():
                if request.session['attempt_join'] == 3:
                    request.session['attempt_join'] = 0
                    needs_captcha = True
                else:
                    request.session['attempt_join'] += 1
            else:
                request.session['attempt_join'] = 1
                needs_captcha = False

            context_dict['alert'] = "successful"

        else:
            # se procesan los errores
            errors = form.errors.as_data()
            if 'captcha' in errors:
                context_dict['alert'] = "needs_captcha"
            elif 'email' in errors:
                if errors['email'][0].code == 'user_exists':
                    context_dict['alert'] = "user_exists"
            print(errors)

    # se vuelve a coger el formulario vacío para presentarlo tanto en un get como en un post.
    form = JoinForm(needs_captcha)
    context_dict['form'] = form
    return render(request, "index.html", context_dict)


def faq(request):
    return render(request, "faq.html")


def faq_english(request):
    return render(request, "faq_english.html")