function Verify(){
  var nickname = $("#nickname").val();
  if (nickname == "")

  {
    $("#need_nickname_error").text("Please provide a nickname!");
    $("#need_nickname_error").fadeIn();
    return false;
  }
  else
  {
    $("#need_nickname_error").text(" ");
    $("#need_nickname_error").fadeOut();
    return true;
    }
  }
}

function Add_Friends() {
  $("#add_friends").fadeIn();
  self.response.write("hey")
  return false;
}

$(document).ready(
  function() {
    $('#setup_form').on('submit', Verify)
    $('#show_add_friends').on('submit', Add_Friends)
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
