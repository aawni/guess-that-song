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
    return Verify_Unique_Send(nickname);
  }
}

function Verify_Unique_Send(nickname) {
  $.post("/searchnickname", {"nickname": nickname}, function(data){
    if (data.is_unique){
      alert("It is unique")
      return true;
    }
    else {
      alert("it is not unique!")
      $("#not_unique_error").text("That nickname is taken. Please enter another!");
      $("#not_unique_error").fadeIn();
      return false;
    }
  });
}

function Show_Add_Friends() {
  $("#add_friends_form").fadeIn(0);
  $("#show_add_friends").fadeOut(0);
  return false;
}

$(document).ready(
  function() {
    $('#setup_form').on('submit', Verify)
    $('#show_add_friends').on('submit', Show_Add_Friends)
  }
);
$('#imageTag').click(function() {
  $("#youTUBE").attr('src', $("#videoContainer iframe", parent).attr('src') + '?autoplay=0');
});
