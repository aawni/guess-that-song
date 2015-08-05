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
