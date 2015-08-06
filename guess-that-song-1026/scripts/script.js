function Verify(e){
  e.preventDefault();
  var nickname = $("#nickname").val();
  var is_new_user = $("#is_new_user").val();
  if (is_new_user=="True"){
    if (nickname == "")
    {
      $("#error").text("Please provide a nickname!");
      $("#error").fadeIn(3000);
      $("#error").fadeOut(3000);
      return false;
    }
    else
    {
      return Verify_Unique(nickname);
    }
  }
  else {
    var genre = $("#genre").val();
    window.location.href = "/quiz?genre="+genre;
  }
}

function Verify_Unique(nickname){
  $.post("/searchnickname", {"nickname": nickname}, function(data){
    if (data.is_unique){
      var genre = $("#genre").val();
      window.location.href = "/quiz?genre="+genre;
    }
    else {
      $("#not_unique_error").text("That nickname is taken. Please enter another!");
      $("#not_unique_error").fadeIn(3000);
      $("#not_unique_error").fadeOut(3000);
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
