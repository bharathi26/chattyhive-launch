from django.core.mail import send_mail

# Create your views here.
from django.shortcuts import render
from launcher.models import InterestedUser


def home(request):
    context_dict = {'need_captcha': False}

    if request.method == 'POST':
        # Getting info from the POST
        email = request.POST.get("email")

        # Creating and saving info in database
        user = InterestedUser()
        user.save()
        user.set_email(email)
        user.set_via('Join')
        user.save()

        if request.session['attempt_join'] >= 1:
            request.session['attempt_join'] += 1
        elif request.session['attempt_join'] == 3:
            request.session['attempt_join'] = 0
            context_dict['need_captcha'] = True
        else:
            request.session['attempt_join'] = 1

        # timestamp = request.POST.get("timestamp")
        # El from@example.com se sustituira por el email que el usuario introduce en el formulario!
        #  y tb se mete despues de "su email es:"
        send_mail('Nueva suscrpcion a chattyhive launch!',
                  'Un nuevo usuario se ha suscrito al lanzamiento, su email es: ' + email,
                  email, ['chattyhive@gmail.com'], fail_silently=False)
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
        #Aqui se mete toda la informacion del formulario en la "seccion escribenos"
        #al asunto le agregamos al final el nombre que dejo en el formulario"
        send_mail(asunto + ' de ' + name, contenido, email, ['chattyhive@gmail.com'],
                  fail_silently=False)
    return render(request, "about.html")


def faq(request):

    return render(request, "faq.html")


def faq_english(request):

    return render(request, "faq_english.html")