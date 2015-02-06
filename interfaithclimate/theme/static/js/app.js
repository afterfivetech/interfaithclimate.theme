$(document).foundation();
$(".select-menu-button").click(function(){
    $("ul.theme_button").slideToggle();
});
$('#mainmenu_area > ul#mainmenu li').each(function(){
    if ($(this).attr('class')=='selected'){
        $("a.select-menu-button > span.holder").html($(' > a > span').html());	
    }
});