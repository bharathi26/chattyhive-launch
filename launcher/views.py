from django.core.mail import send_mail

# Create your views here.
from django.shortcuts import render
from launcher.models import InterestedUser
from .forms import JoinForm


def home(request):
    context_dict = {'alert': 'no'}
    needs_captcha = False

    if request.method == 'POST':
        # Getting info from the POST
        form = JoinForm(needs_captcha, request.POST)

        if form.is_valid():
            # We save what we receive in the form and that is already associated with InterestedUser model
            print("formulario válido!", form.cleaned_data['email'])
            form.save(commit=True)

            send_mail('Nueva suscrpcion a chattyhive launch!',
                      'Un nuevo usuario se ha suscrito al lanzamiento, su email es: ' + form.cleaned_data['email'],
                      form.cleaned_data['email'], ['chattyhive@gmail.com'], fail_silently=False)

            # We only want to show captcha if it is the third time an email is registered
            if 'attempt_join' in request.session.keys():
                if request.session['attempt_join'] == 3:
                    request.session['attempt_join'] = 0
                    needs_captcha = True
                else:
                    request.session['attempt_join'] += 1
            else:
                request.session['attempt_join'] = 1
        else:
            # se procesan los errores
            errors = form.errors.as_data()
            i = 0
            for error in errors:
                print("error{0}: {1}: {2}".format(i, error, error[i]))
                i += 1

    # se vuelve a coger el formulario vacío para presentarlo tanto en un get como en un post.
    form = JoinForm(needs_captcha)
    context_dict['form'] = form
    return render(request, "index.html", context_dict)


def about(request):
    if request.method == 'POST':
        # Getting info from the POST
        name = request.POST.get("name")
        email = request.POST.get("email")
        asunto = request.POST.get("asunto")
        contenido = request.POST.get("contenido")

        # Creating and saving info in database
        user = InterestedUser()
        user.save()
        user.set_name(name)
        user.set_email(email)
        user.set_subject(asunto)
        user.set_content(contenido)
        user.set_via('Escribenos')
        user.save()

        # timestamp = request.POST.get("timestamp")
        # Aqui se mete toda la informacion del formulario en la "seccion escribenos"
        # al asunto le agregamos al final el nombre que dejo en el formulario"
        send_mail(asunto + ' de ' + name, contenido, email, ['chattyhive@gmail.com'],
                  fail_silently=False)
    return render(request, "about.html")


def faq(request):
    return render(request, "faq.html")


def faq_english(request):
    return render(request, "faq_english.html")