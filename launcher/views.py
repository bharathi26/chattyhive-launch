from django.core.mail import send_mail

# Create your views here.
from django.shortcuts import render
from launcher.models import InterestedUser
from .forms import JoinForm, ContactForm


def about(request):
    context_dict = {'alert': 'nothing'}
    needs_captcha = False

    if request.method == 'POST':
        # Getting info from the POST
        form = ContactForm(needs_captcha, request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            # We save what we receive in the form and that is already associated with InterestedUser model
            form.save(commit=True)
            send_mail(form.cleaned_data['subject'] + ' de ' + form.cleaned_data['name'], form.cleaned_data['contenido'],
                      form.cleaned_data['email'], ['chattyhive@gmail.com'],
                      fail_silently=False)
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

            context_dict['alert'] = "successful"

        else:
            # se procesan los errores
            errors = form.errors.as_data()
            print(errors)
            if 'captcha' in errors and 'email' not in errors:
                email = form.data['email']
                context_dict['alert'] = "needs_captcha"
                form = ContactForm(needs_captcha)
                form.data['email'] = email
                context_dict['form'] = form
                return render(request, "about.html", context_dict)
    form = ContactForm(needs_captcha)
    context_dict['form'] = form
    return render(request, "about.html", context_dict)


def home(request):
    context_dict = {'alert': 'nothing'}
    needs_captcha = False

    if request.method == 'POST':
        # Getting info from the POST
        form = JoinForm(needs_captcha, request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            # We save what we receive in the form and that is already associated with InterestedUser model
            form.save(commit=True)

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

            context_dict['alert'] = "successful"

        else:
            # se procesan los errores
            errors = form.errors.as_data()
            print(errors)
            if 'captcha' in errors and 'email' not in errors:
                email = form.data['email']
                context_dict['alert'] = "needs_captcha"
                form = JoinForm(needs_captcha)
                form.data['email'] = email
                context_dict['form'] = form
                return render(request, "index.html", context_dict)

    # se vuelve a coger el formulario vacío para presentarlo tanto en un get como en un post.
    form = JoinForm(needs_captcha)
    context_dict['form'] = form
    return render(request, "index.html", context_dict)


def faq(request):
    return render(request, "faq.html")


def faq_english(request):
    return render(request, "faq_english.html")