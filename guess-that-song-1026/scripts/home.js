//home
function Verify(e){
  e.preventDefault();
  var nickname = $("#nickname").val();
  var no_nickname = $("#no_nickname").val();
  if (no_nickname=="True"){
    if (nickname == "")
    {
      $("#home_error").text("Please provide a nickname!");
      $("#home_error").fadeIn(1000);
      $("#home_error").fadeOut(3000);
      return false;
    }
    else
    {
      return VerifyUnique(nickname);
    }
  }
  else {
    var genre = $("#genre").val();
    window.location.href = "/quiz?genre="+genre;
  }
}
//home
function VerifyUnique(nickname){
  $.post("/searchnickname", {"nickname": nickname}, function(data){
    if (data.is_unique){
      window.location.href = "/home";
    }
    else {
      $("#home_error").text("That nickname is taken. Please enter another!");
      $("#home_error").fadeIn(1000);
      $("#home_error").fadeOut(3000);
    }
  });
}

function VerifyContinue() {
  var no_nickname = $("#no_nickname").val();
  if (no_nickname=="True") {
    $("#home_error").text("You must provide a unique nickname before you can play!");
    $("#home_error").fadeIn(1000);
    $("#home_error").fadeOut(3000);
    return false;
  }
}

//all
$(document).ready(
  function() {
    $('#nickname_form').on('submit', Verify)
    $('#setup_form').on('submit',VerifyContinue)
    $(".big_btn").hover(function(){
    $(this).css("background", "#6495ED");
    }, function(){
    $(this).css("background", "white");
  });
});
