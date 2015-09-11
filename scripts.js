
jQuery(document).ready(function() {

    /*
        Background slideshow
    */
    $.backstretch([
    "/static/img/backgrounds/5_11.jpg"
    , "/static/img/backgrounds/ruta.jpg"
    , "/static/img/backgrounds/Ruta-66-EEUU.jpg"
    ], {duration: 3000, fade: 1000});

    /*
        Tooltips
    */
    $('.links a.home').tooltip();
    $('.links a.blog').tooltip();

    /*
        Form validation
    */
    $('.register form').submit(function(){
        $(this).find("label[for='Usuario']").html('Usuario');
        $(this).find("label[for='password']").html('Password');
        ////
        var Usuario = $(this).find('input#Usuario').val();
        var password = $(this).find('input#password').val();
        if(Usuario == '') {
            $(this).find("label[for='Usuario']").append("<span style='display:none' class='green'> - Por Favor Ingrese su Usuario.</span>");
            $(this).find("label[for='Usuario'] span").fadeIn('medium');
            return false;
        }
        if(password == '') {
            $(this).find("label[for='password']").append("<span style='display:none' class='green'> - Ingrese un Password Valido.</span>");
            $(this).find("label[for='password'] span").fadeIn('medium');
            return false;
        }
    });


});



