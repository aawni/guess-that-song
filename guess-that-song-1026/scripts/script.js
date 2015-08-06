function Verify(){
  var nickname = $("#nickname").val();
  var is_new_user = $("#is_new_user").val();
  if (is_new_user){
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
      return Verify_Unique(nickname);
    }
  }
}

function Verify_Unique(nickname){
  $.post("/searchnickname", {"nickname": nickname}, function(data){
    if (data.is_unique){
      alert("it is unique!")
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
