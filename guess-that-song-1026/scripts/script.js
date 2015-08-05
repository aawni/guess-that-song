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
