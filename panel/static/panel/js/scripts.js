// when bars is clicked
$(document).ready(function () {
    $('.navbar-brand').click(function (e) { 
        e.preventDefault();
        
        $('.sidebar').toggleClass("active");
        $('.content').toggleClass("active");
    });

    
    
});

$('.icon-close').click(function (e) { 
    e.preventDefault();
    alert("success");

    // $('.sidebar').removeClass("active");
    // $('.content').removeClass("active");
});