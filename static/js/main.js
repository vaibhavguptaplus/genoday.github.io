$(document).ready(function(){


$(".text").typed({
    strings:["YOUR <strong class='primary'>VISION. </strong> ","OUR<strong class='primary'> MISSION. </strong>"],
    typeSpeed:0,
    loop:true,
});
$(window).scroll(function(){
    var top=$(window).scrollTop();
    if(top>=60){
        $('nav').addClass('secondary');
    }
    else
        if($("nav").hasClass('secondary')){
            $("nav").removeClass('secondary');
        
    }
});

$('.accordion-header').click(function(){
    $('.accordion .accordion-body').slideUp();
    $(this).next('.accordion-body').slideDown();
    $('.accordion .accordion-header span').text('+');
    $(this).children('span').text('-');
  });
  
  $('.work').magnificPopup({
    delegate: 'a', // child items selector, by clicking on it popup will open
    type: 'image',
    gallery: {
        enabled: true
      }
    // other options
  });

 
  
  
});    


  