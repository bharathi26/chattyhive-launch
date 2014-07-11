/**
 * Created with PyCharm.
 * User: xurxo
 * Date: 15/02/14
 * Time: 19:34
 * To change this template use File | Settings | File Templates.
 */
// Buttons behaviour
    $(document).ready(function() {
        // Button send behaviour when clicked
        $('#btn_send').on('click', function()
        {
            var email = $("#email").val();
            if(!validarEmail(email)) {
                return false;
            }
            $("#email").val("");
            var d = new Date();
            var timestamp = d.toTimeString();
            var csrftoken = $.cookie('csrftoken');
            $.ajax({
                type: "POST",
                url: "/",
                headers: {"X-CSRFToken":csrftoken},
                data: {timestamp:timestamp, email:email},
                success: function(){
                        alert("Gracias! Hemos recibido tu email! Pronto te enviaremos instrucciones para descargar la app y ser beta tester.")
                    },
                failure: function(errMsg) {
                        alert("Uuups! Algo ha ido mal :S Env&iacute;anos el email otra vez!")
                    }
            });
            return false;
        });
    });

// Validates the email
function validarEmail( email ) {
    var expr = /^([a-zA-Z0-9_\.\-])+\@(gmail.com)+$/;
    if ( !expr.test(email) ) {
        alert("La dirección de correo " + email + " es incorrecta o no es de gmail. Por favor introduce el email que usas en tu dispositivo Android.");
        return false;
    } else {
        return true;
    }
}