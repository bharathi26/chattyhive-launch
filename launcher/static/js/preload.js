/**
 * Created by diego on 22/01/14.
 */

this.addEventListener("DOMContentLoaded", preloadImages, true);

function preloadImages(e) {
    var imageArray = new Array(STATIC_URL + "images/isotipo_sombreado_sin_gradiente_transparente-02.png");

    for (var i = 0; i < imageArray.length; i++) {
        var tempImage = new Image();
        tempImage.src = imageArray[i];
    }
}