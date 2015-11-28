$(document).ready(function () {

    var badgeRight = $("#badge-right");
    var noDisponible = $(".tool");
    var triangulo = $(".triangulo");
    
    badgeRight.on("mouseover", function() {
        noDisponible.fadeIn("fast");
        triangulo.fadeIn("fast");
    });
    badgeRight.on("mouseout", function() {
        noDisponible.fadeOut("fast");
        triangulo.fadeOut("fast");
    });

});