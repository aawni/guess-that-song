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
