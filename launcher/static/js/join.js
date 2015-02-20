/**
 * Created with PyCharm.
 * User: Diego
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
            contenido_bocadillo = "Introduce la cuenta de Google asociada a tu dispositivo Android."
            mostrarBocadillo()
        })
    });

    $('#btn_send').on('click', function()
    {
        var email = $("#id_email").val();
        if(!validarEmail(email)) {
            return false;
        }
        return true
    });
});


function mostrarBocadillo() {
    shown ?
        $('#id_email').hideBalloon() :
        $('#id_email').showBalloon({
            classname: "balloon",
            contents: contenido_bocadillo,
            position: "top",
            offsetX: 0,
            offsetY: 5,
            tipSize: 20,
            showDuration: 100,
            css: {
                maxWidth: "17em",
                border: "solid 1px orange",
                color: "#222",
                fontWeight: "bold",
                fontSize: "130%",
                backgroundColor: "#fff",
                padding: "10px"
            }
        });
    shown = !shown;
}

// Validates the email
function validarEmail( email ) {
    var expr = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    if ( !expr.test(email) ) {
        contenido_bocadillo = "La dirección de correo no tiene un formato válido. Por favor introduce el email que usas en tu dispositivo Android."
        shown = false
        mostrarBocadillo()
        return false;
    } else {
        return true;
    }
}