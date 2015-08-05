function Verify(){
  var nickname = $("#nickname").val();
  console.log(nickname);
  if (nickname == "")

  {
    $("#error").text("Please provide a nickname!");
    $("#error").fadeIn();
    return false;
  }
  else
  {
    $("#error").text(" ");
    $("#error").fadeOut();
    return true;
  }
}

$(document).ready(
  function() {
    $('#setup_form').on('submit', Verify)
  }
);
$('#imageTag').click(function() {
  $("#youTUBE").attr('src', $("#videoContainer iframe", parent).attr('src') + '?autoplay=0');
});

// jQuery('a.introVid').click(function(){
//   autoPlayVideo(  "#videoContainer",'450','283');
// });
// function autoPlayVideo(vcode, width, height){
//   "use strict";
//   $("#videoContainer").html('<iframe width="'+width+'" height="'+height+'" src="https://www.youtube.com/embed/'+vcode+'?autoplay=1&loop=1&rel=0&wmode=transparent" frameborder="0" allowfullscreen wmode="Opaque"></iframe>');
// }
