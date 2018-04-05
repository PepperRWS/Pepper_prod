
var addresetButton= function(session,position,timeout,callback) {
  callback = callback || 0;
  $( document ).ready(function() {
    //$( "body" ).append( "<div class='button resetbutton fa fa-home resetbutton_"+position+"'></div>" );
    $( "body" ).append('<a class="btn-floating waves-effect waves-light resetbutton resetbutton_'+position+' blue "><div class="fa fa-home resetbutton_icon"></div></a>')

    session.socket().on('touchstart', function () {
      //alert("connected");
    });

    $.when( session.service("ALMemory") ).then(function(mem){

      $( ".resetbutton" ).one("touchstart",function(){
        try{
          mem.raiseEvent("Decos/all/reset","1");
        } catch(error){
          alert(error);
        }
      });

    });
  });

  //auto reset after 60s of inactivity
  timeout_timer = null
  this.resetTimer = function(timeout){

    if(timeout_timer){
      console.log("Clearing old timeout timer ")
      clearTimeout(timeout_timer)
    }
    timeout_timer =  setTimeout(function(){
      console.log("Reseting! ")

      if(!callback)
        $( ".resetbutton" ).trigger( "touchstart" );
      else
        callback()

    }, timeout);
  }
  console.log("Setting reset timeout to "+timeout)
  this.resetTimer(timeout);

  return this;
}
