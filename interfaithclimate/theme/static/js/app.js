$(document).foundation({
    orbit: {
    animation: 'fade',
    timer_speed: 5000,
    pause_on_hover: true,
    resume_on_mouseout: true,
    animation_speed: 500,
    navigation_arrows: true,
    bullets: true,
    slide_number: false,
    timer: true,
  }    
});
$(".select-menu-button").click(function(){
    $("ul.theme_button").slideToggle();
});
$('#mainmenu_area > ul#mainmenu li').each(function(){
    if ($(this).attr('class')=='selected'){
        $("a.select-menu-button > span.holder").html($(' > a',this).html());	
    }
});

$('.if-accordion').find('.accord-header').click(function(){
    
    //Expand or collapse this panel
    $(this).next().slideToggle('slow');

    //Hide the other panels
    $(".accord-content").not($(this).next()).slideUp('slow');

});