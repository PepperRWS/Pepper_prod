/*
* THIS IS ONLY USED FOR THE RESET BUTTON AT THE MOMENT
*/

$( document ).ready(function() {
  //alert('bclick ready!');

  $('body').on('touchstart', '.button', function () {
    $(this).addClass('animation-bclick');
    //$(this).css("animation-duration",'2s');
  });

});
