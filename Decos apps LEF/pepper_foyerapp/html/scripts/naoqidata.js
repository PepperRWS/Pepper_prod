

function Tablet(){
  var session = new QiSession("198.18.0.1");
  this.session= session;

  session.socket().on('connect', function () {
    //Nothing TODO here
  });

  this.setLogo = function(id){
    $.when( session.service("ALMemory") ).then(function(mem){
      mem.getData("Decos/client/banner").then(function(url){
        $('#'+id).attr("src","resources/"+url);
      });
    });
  }

  this.setWelcomeText = function(id){
    $.when( session.service("ALMemory") ).then(function(mem){
      $.when(mem.getData("Decos/client/welcome_text"),mem.getData("Decos/client/welcome_text/show"),mem.getData("Decos/client/welcome_text/size")).then(function(text,show,size){
        if(show){
          $('#'+id).css("font-size", size+ "px");
          $('#'+id).html(text);
        }
      });
    });
  }

  this.setVisitor = function(id){
    $.when( session.service("ALMemory") ).then(function(mem){
      mem.getData("Decos/mod4/visitor").then(function(name){
        $('#'+id).html(name);
      });
    });
  }

  this.setVisitorInput = function(id){
    $.when( session.service("ALMemory") ).then(function(mem){
      mem.getData("Decos/mod4/visitor").then(function(name){
        $('#'+id).val(name);
      });
    });
  }

  this.setEmployee= function(id){
    $.when( session.service("ALMemory") ).then(function(mem){
      mem.getData("Decos/mod4/employee").then(function(name){
        $('#'+id).html(name);
      });
    });
  }

  this.setEmployeePicture = function(id){
    $.when( session.service("ALMemory") ).then(function(mem){
      mem.getData("Decos/mod4/employee/picture").then(function(picture){
        var image = new Image();
        image.src= 'data:image/png;base64,'+picture;
        $('#'+id).attr("src",image.src);
      });
    });
  }

  var raiseEvent = function(event,value){
    $.when( session.service("ALMemory") ).then(function(mem){
      mem.raiseEvent(event,value);
    });
  };
  this.raiseEvent= raiseEvent;

  this.registerTounch = function(id){
    $.when( session.service("ALMemory") ).then(function(mem){
      $( "#"+id ).on("touchstart",function(){
        mem.raiseEvent("Decos/mod1/Tablet/touch",1);
      });
    });
  }

  this.showQuestions = function(id){
    $.when( session.service("ALMemory") ).then(function(mem){
      $.when(mem.getData("Decos/mod2/bulletquestions"),mem.getData("Decos/mod2/bulletquestions/important")).then(function(questions,important){
        var quest_list = questions.split(';');
        var imp_quest_list = important.split(';');

        for(var i=0; i < quest_list.length ; i++){
          $( "#"+id ).append("<div class='button question' id='question"+i+"' value='"+i+"'>"+quest_list[i]+"</div>");

          if($.inArray(quest_list[i], imp_quest_list) > -1)
            $( "#question"+i ).css("width","1640px");

          $( "#question"+i ).bind('touchstart', {value: i+1} ,function(event){
            raiseEvent("Decos/mod2/Tablet/touch", String(event.data.value) );
          });
        }
      });
    });
  };

  this.setText = function(id,key){
    $.when( session.service("ALMemory") ).then(function(mem){
      mem.getData(key).then(function(text){
        $('#'+id).html(text);
      });
    });
  }

  this.setImg = function(id,key){
    $.when( session.service("ALMemory") ).then(function(mem){
      mem.getData(key).then(function(url){
        $('#'+id).attr("src","resources/"+url);
      });
    });
  }

  this.setTitle = function(id){
    $.when( session.service("ALMemory") ).then(function(mem){
      mem.getData("Decos/mod2/title").then(function(qtitle){
        $('#'+id).html("<p>"+qtitle+"</p>");
      });
    });
  }

  this.setQuestion = function(id){
    $.when( session.service("ALMemory") ).then(function(mem){
      mem.getData("Decos/mod301/question/title").then(function(qtitle){
        $('#'+id).html(qtitle);
      });
    });
  }

  this.sendAnswer = function(event,value){
    $.when( session.service("ALMemory") ).then(function(mem){
      //alert();
      mem.raiseEvent(event,value);
    });
  }

  this.getPlaceInLine = function(){
    $.when( session.service("ALMemory") ).then(function(mem){
      mem.getData("Decos/mod5/visitor_place").then(function(number){
        $('#place_line').html(number);
      });
    });
  }

  /*Module 6*/
  this.showImages = function(id){
    $.when( session.service("ALMemory") ).then(function(mem){
      $.when(mem.getData("Decos/mod6/images")).then(function(images){
        var img_list = images.split(';');
        for(var i=0; i < img_list.length ; i++)
          $( "#"+id ).append("<div class='mod6-fa-img fa "+img_list[i]+"'></div>");
      });
    });
  }


  this.showText = function(id){
    $.when( session.service("ALMemory") ).then(function(mem){
      $.when(mem.getData("Decos/mod6/text")).then(function(text){
        var text_list = text.split(';');
        for(var i=0; i < text_list.length ; i++)
          $( "#"+id ).append("<div class='mod6-text' >"+text_list[i]+"</div>");
      });
    });
  }

  /* Module 4 */
  this.subscribeToVar = function(id,variable){
    $.when( session.service("ALMemory") ).then(function(mem){
      mem.subscriber(variable).done(function (subscriber) {
          subscriber.signal.connect(function (state) {
            $('#'+id).html(state);
          });
      });
    });
  }

  //Listens to a key and runs a function on event
  this.subscribeFunction = function(func,key){
    $.when( session.service("ALMemory") ).then(function(mem){
      mem.subscriber(key).done(function (subscriber) {
          subscriber.signal.connect(function (state) {
            func(state);
          });
      });
    });
  }

  /* * */

  var paintStars = function(till){
    for(var i=1; i<= till; i++)
      $( "#star"+i ).css("color","#FFD85E");

    $.when( session.service("ALMemory") ).then(function(mem){
      mem.raiseEvent("Decos/mod7/score",till);
    });
  }

  var onStarTouch = function(event){
    var star_number = event.data.star_number;
    paintStars(star_number);
  };

  this.listenStarTouch = function(){
    $.when( session.service("ALMemory") ).then(function(mem){
      for(var i=1; i<= 5; i++)
        $( "#star"+i ).on("touchstart", {star_number: i} , onStarTouch);
    });
  };
}
