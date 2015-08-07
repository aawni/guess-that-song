function Verify(e){
  e.preventDefault();
  var nickname = $("#nickname").val();
  var no_nickname = $("#no_nickname").val();
  if (no_nickname=="True"){
    if (nickname == "")
    {
      $("#error").text("Please provide a nickname!");
      $("#error").fadeIn(1000);
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
      $("#not_unique_error").fadeIn(1000);
      $("#not_unique_error").fadeOut(3000);
    }
  });
}

function Verify_Friend(e){
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
      return Verify_No_Repeat(friend_nickname);
    }
}

function Verify_No_Repeat(friend_nickname){
  $.post("/friends", {"friend_nickname": friend_nickname}, function(data){
    if (data.repeat)
    {
      $("#repeat_error").text("You are already friends with them!");
      $("#repeat_error").fadeIn(1000);
      $("#repeat_error").fadeOut(3000);
    }
    else {
      window.location.href = "/friends";
      }

  });
}

function Show_Add_Friends() {
  $("#add_friends_form").fadeIn(0);
  $("#show_add_friends").fadeOut(0);
  return false;
}

function Show_Answers(e){
  e.preventDefault();
  $("#users_answers").fadeIn(0);
  $("#show_answers").fadeOut(0);
  return false;
}
function Show_Jordan(e){
  e.preventDefault();
  $("#jordan_div").toggle();
  return false;
}
function Show_Alia(e){
  e.preventDefault();
  $("#alia_div").toggle();
  return false;
}
function Show_Jewel(e){
  e.preventDefault();
  $("#jewel_div").toggle();
  return false;
}


$(document).ready(
  function() {
    $('#setup_form').on('submit', Verify)
    $('#show_add_friends').on('submit', Show_Add_Friends)
    $('#show_answers').on('submit', Show_Answers)
    $(".big_btn").hover(function(){
    $(this).css("background", "#6495ED");
    }, function(){
    $(this).css("background", "white");
  });
    $("#show_answers_button").hover(function(){
      $(this).css("background", "#6495ED");
    }, function(){
      $(this).css("background", "white");
    });
    $('#show_jordan').on('submit',Show_Jordan)
    $('#show_alia').on('submit',Show_Alia)
    $('#show_jewel').on('submit',Show_Jewel)
    $('#add_friends_form').on('submit', Verify_Friend)
});
// $('#imageTag').click(function() {
//   $("#youTUBE").attr('src', $("#videoContainer iframe", parent).attr('src') + '?autoplay=0');
// });
// $( '#timer-countup' ).countdown( {
//   from: 0,
//   to: 180,
//   autostart: true
// } );



// $( '#timer-outputpattern' ).countdown( {
//   outputPattern: '$day Days $hour Hours $minute Miniuts $second Seconds',
//   from: 60 * 60 * 24 * 3
// } );
