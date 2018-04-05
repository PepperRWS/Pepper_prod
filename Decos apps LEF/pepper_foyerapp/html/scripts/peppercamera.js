
$( document ).ready(function() {

  //alert(window.screen.availHeight + "/"+ window.screen.availWidth);

  var session = new QiSession("198.18.0.1");
  //var session = new QiSession('10.180.10.245');
  var canvas = document.getElementById("camera_stream");
  var resolution = 0;
  var frameRate = 3;
  var width = 160;
  var height = 120;

  canvas.width = width;
  canvas.height = height;
  var ctx = canvas.getContext("2d");
  // var globalVideo, globalCamera;

  session.socket().on('connect', function(){
    console.log("QiSession connected");
    var img = new Image();
    //ctx.drawImage(img, 0, 0);

    session.service("ALVideoDevice").done(function(video){
      //http://doc.aldebaran.com/2-1/naoqi/vision/alvideodevice-api.html#ALVideoDeviceProxy::subscribeCamera__ssCR.iCR.iCR.iCR.iCR
      video.subscribeCamera("10", 0, resolution, 11, frameRate).then(function(camera) {
        setInterval(function() {
          getImage(camera, video);
        }, 333);

        function closeCamera() {
          video.unsubscribe(camera);
        }

        window.onbeforeunload = function (ev) {
          closeCamera();
        }
      });

    });
  }).on('disconnect', function(){
    console.log("QiSession disconnect");
  });

  function speak(text){
    session.service("ALTextToSpeech").done(function(tts){
      tts.say(text);
    });
  }

  function getImage(camera, video) {
    video.getImageRemote(camera).then(function (imageData) {
      //console.log("Received something");
      if (imageData) {
        //alert();
        //console.log("Received an image");
        showImage(imageData);
      }
    });
  }

  function showImage(data) {
    var binData = window.atob(data[6]);
    var buffer = new ArrayBuffer(4 * width * height);
    var rgbaData = new Uint8ClampedArray(buffer);
    for (var i = 0; i < width*height; i++) {
      rgbaData[i*4] = binData.charCodeAt(i*3);
      rgbaData[i*4+1] = binData.charCodeAt(i*3+1);
      rgbaData[i*4+2] = binData.charCodeAt(i*3+2);
      rgbaData[i*4+3] = 255;
    }
    try{
      //var imgData = new ImageData(rgbaData, width, height);
      var imgData= ctx.createImageData(width, height);
      imgData.data.set(rgbaData);
    } catch(err){
      alert(err.message);
    }
    ctx.putImageData(imgData, 0, 0);
  }

});
