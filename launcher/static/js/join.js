/**
 * Created with PyCharm.
 * User: xurxo
 * Date: 15/02/14
 * Time: 19:34
 * To change this template use File | Settings | File Templates.
 */

// If we click in any other part of the document and the Balloon was shown it will be hidden
var shown = false;
var contenido_bocadillo = "empty"

$(document).click(function(event) {
    if(!$(event.target).closest('#id_email').length) {
        if($('.balloon').is(":visible")) {
            $('.balloon').hide()
            shown = false;
        }
    }
})

// Buttons behaviour
$(document).ready(function() {
    // Button send behaviour when clicked

    $(function() {
        $('#id_email').on("click", function() {
            contenido_bocadillo = "Introduce la cuenta de Google asociada a tu dispositivo Android"
            mostrarBocadillo()
        })
    });

    $('#btn_send').on('click', function()
    {
        var email = $("#id_email").val();
        if(!validarEmail(email)) {
            return false;
        }
        $("#id_email").val("");
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


function mostrarBocadillo() {
    shown ?
        $('#id_email').hideBalloon() :
        $('#id_email').showBalloon({
            classname: "balloon",
            contents: contenido_bocadillo,
            position: "top",
            offsetX: 50,
            offsetY: 5,
            tipSize: 20,
            showDuration: 100,
            css: {
                maxWidth: "17em",
                border: "solid 1px orange",
                color: "#463974",
                fontWeight: "bold",
                fontSize: "130%",
                backgroundColor: "#efefef"
            }
        });
    shown = !shown;
}

// Validates the email
function validarEmail( email ) {
    var expr = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    if ( !expr.test(email) ) {
        contenido_bocadillo = "La dirección de correo " + email + " es incorrecta o no es de gmail. Por favor introduce el email que usas en tu dispositivo Android."
        shown = false
        mostrarBocadillo()
        return false;
    } else {
        return true;
    }
}