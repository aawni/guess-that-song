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
      $("#not_unique_error").fadeIn(1000);
      $("#not_unique_error").fadeOut(3000);
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
    $('#show_jordan').on('submit', Show_Jordan)
    $('#show_alia').on('submit', Show_Alia)
    $('#show_jewel').on('submit', Show_Jewel)
});
// $('#imageTag').click(function() {
//   $("#youTUBE").attr('src', $("#videoContainer iframe", parent).attr('src') + '?autoplay=0');
// });
$( '#timer-countup' ).countdown( {
  from: 0,
  to: 180,
  autostart: true
} );



$( '#timer-outputpattern' ).countdown( {
  outputPattern: '$day Days $hour Hours $minute Miniuts $second Seconds',
  from: 60 * 60 * 24 * 3
} );
