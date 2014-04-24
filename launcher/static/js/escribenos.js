/**
 * Created with PyCharm.
 * User: xurxo
 * Date: 15/02/14
 * Time: 20:57
 * To change this template use File | Settings | File Templates.
 */
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
        $('#btn_send2').on('click', function()
        {
            var name = $("#name").val();
            var email = $("#email").val();
            var asunto = $("#asunto").val();
            var contenido = $("#contenido").val();
            var d = new Date();
            var timestamp = d.toTimeString();
//            var csrftoken = $.cookie('csrftoken');
            alert("Gracias! Hemos recibido tu email!");
            $.ajax({
                type: "POST",
                url: "/about",
                headers: {"X-CSRFToken":csrftoken},
                data: {timestamp:timestamp, name:name,
                    email:email, asunto:asunto, contenido:contenido},
                success: function(){
                        alert("Gracias! Hemos recibido tu email!")
                    },
                failure: function(errMsg) {
                        alert("Uuups! Algo ha ido mal :S Env&iacute;anos el email otra vez!")
                    }
            });
            return false;
        });
    });