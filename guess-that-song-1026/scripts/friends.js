
//friends
function VerifyFriend(e){
  e.preventDefault();
  var friend_nickname = $("#friend_nickname_jquery").val();
  if (friend_nickname == "")
    {
      $("#friend_error").text("Please provide a nickname!");
      $("#friend_error").fadeIn(1000);
      $("#friend_error").fadeOut(3000);
      return false;
    }
  else
    {
      return VerifyNoRepeat(friend_nickname);
    }
}
//friends
function VerifyNoRepeat(friend_nickname){
  $.post("/friends", {"friend_nickname": friend_nickname}, function(data){
    if (data.repeat)
    {
      $("#repeat_error").text("You are already friends with them!");
      $("#repeat_error").fadeIn(1000);
      $("#repeat_error").fadeOut(3000);
    }
    else if (data.is_self)
    {
      $("#self_error").text("You can't add yourself stupid!");
      $("#self_error").fadeIn(1000);
      $("#self_error").fadeOut(3000);
    }
    else if (!data.is_valid)
    {
      $("#valid_error").text("That nickname doesn't exist!");
      $("#valid_error").fadeIn(1000);
      $("#valid_error").fadeOut(3000);
    }
    else {
      window.location.href = "/friends";
      }

  });
}
//friends
function ShowAddFriends() {
  $("#add_friends_form").fadeIn(0);
  $("#show_add_friends").fadeOut(0);
  return false;
}
//friends
function NotifyDelete(e){
  e.preventDefault();
  var delete_friend_id = $("#delete_friend_id").val();
  $.post("/delete", {"delete_friend_id": delete_friend_id}, function(data){
      alert("You are no longer friends with " + data.friend_nickname + "!" )
      window.location.href = "/friends";
  });
}
//all
$(document).ready(
  function() {
    $('#show_add_friends').on('submit', ShowAddFriends)
    $('#add_friends_form').on('submit', VerifyFriend)
    $('#delete').on('submit', NotifyDelete)
    $(".big_btn").hover(function(){
    $(this).css("background", "#6495ED");
    }, function(){
    $(this).css("background", "white");
  });
});
