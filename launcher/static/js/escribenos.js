/**
 * Created with PyCharm.
 * User: Diego
 * To change this template use File | Settings | File Templates.
 */

// If we click in any other part of the document and the Balloon was shown it will be hidden
var shown = false;
var contenido_bocadillo2 = "empty"

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

    $('#btn_send2').on('click', function()
    {
        var email = $("#id_email").val();
        if(!validarEmail(email)) {
            return false;
        }
        var nombre = $("#id_name").val();
        if(!validarNombre(nombre)) {
            return false;
        }
        var subject = $("#id_subject").val();
        if(!validarAsunto(subject)) {
            return false;
        }
        var content = $("#id_content").val();
        if(!validarContenido(content)) {
            return false;
        }
        return true
    });
});


function mostrarBocadillo( id_elemento ) {
    shown ?
        $(id_elemento).hideBalloon() :
        $(id_elemento).showBalloon({
            classname: "balloon",
            contents: contenido_bocadillo2,
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
        contenido_bocadillo2 = "La dirección de correo no tiene un formato válido."
        shown = false
        mostrarBocadillo('#id_email')
        return false;
    } else {
        return true;
    }
}

function validarNombre( nombre ) {
    if ( nombre.length == 0) {
        contenido_bocadillo2 = "Este campo no puede estar vacío"
        shown = false
        mostrarBocadillo('#id_name')
        return false;
    } else if ( nombre.length > 128 ) {
        contenido_bocadillo2 = "El campo Nombre no debe ocupar más de 128 letras"
        shown = false
        mostrarBocadillo('#id_name')
        return false;
    } else {
        return true;
    }
}

function validarAsunto( asunto ) {
    if ( asunto.length > 256 ) {
        contenido_bocadillo2 = "El campo Asunto no debe ocupar más de 256 letras"
        shown = false
        mostrarBocadillo('#id_subject')
        return false;
    } else {
        return true;
    }
}

function validarContenido( contenido ) {
    if ( contenido.length == 0) {
        contenido_bocadillo2 = "Este campo no puede estar vacío"
        shown = false
        mostrarBocadillo('#id_content')
        return false;
    } else if ( contenido.length > 1000 ) {
        contenido_bocadillo2 = "El campo Contenido no debe ocupar más de 1000 letras"
        shown = false
        mostrarBocadillo('#id_content')
        return false;
    } else {
        return true;
    }
}