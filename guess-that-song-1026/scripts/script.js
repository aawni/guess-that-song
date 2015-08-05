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
    return true;
    window.location= "/quiz";
  }

$(document).ready(
  function() {
    $('#setup_form').on('submit', Verify)
  }
);
