
//results
function Show_Answers(e){
  e.preventDefault();
  $("#users_answers").toggle();
  return false;
}
//all
$(document).ready(
  function() {
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
});
