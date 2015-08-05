function Verify(){
  var nickname = $("#nickname").val();
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
    Verify_Unique_Send(nickname);
  }
}

function Verify_Unique_Send(nickname) {
  $.post("/searchnickname", {"nickname": nickname}, function(data){
    if (data.is_unique){
      return true;
    }
    else (
      $("#not_unique_error").text("That nickname is taken. Please enter another!");
      $("#not_unique_error").fadeIn();
      return false;
    )
  })
}

function Show_Add_Friends() {
  $("#add_friends_form").fadeIn(0);
  $("#show_add_friends").fadeOut(0);
  return false;
}

$(document).ready(
  function() {
    $('#setup_form').on('submit', Verify)
    $('#show_add_friends').click(Show_Add_Friends)
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
