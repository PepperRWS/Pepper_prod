$( document ).ready(function() {
  $( "body" ).append( "<div class='button resetbutton fa fa-home'></div>" );

  tablet.session.socket().on('connect', function () {
    //alert("connected");
  });

  $( ".resetbutton" ).on("touchstart",function(){
    try{
      tablet.raiseEvent("Decos/all/reset","1");
    } catch(error){
      alert(error);
    }
  });

  //auto reset after 60s of inactivity
  setTimeout(function(){
    $( ".resetbutton" ).trigger( "touchstart" );
  }, 90000);
});
