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
    users_with_same_nickname=UserModel.query().filter(UserModel.nickname==nickname).fetch();
          console.log(users_with_same_nickname)
    if (users_with_same_nickname!=[])
    {

      $("#need_unique_nickname_error").text("Sorry, that nickname is taken. Please change your nickname so it is unique!");
      $("#need_unique_nickname_error").fadeIn();
      return false;
    }
    else
    {
      $("#need_unique_nickname_error").text(" ");
      $("#need_unique_nickname_error").fadeOut();
      return true;
    }
  }
}

$(document).ready(
  function() {
    $('#setup_form').on('submit', Verify)
  }
);
