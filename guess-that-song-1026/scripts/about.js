//about
function Show_Jordan(e){
  e.preventDefault();
  $("#jordan_div").toggle();
  return false;
}
//about
function Show_Alia(e){
  e.preventDefault();
  $("#alia_div").toggle();
  return false;
}
//about
function Show_Jewel(e){
  e.preventDefault();
  $("#jewel_div").toggle();
  return false;
}

//all
$(document).ready(
  function() {
    $('#show_jordan').on('submit',Show_Jordan)
    $('#show_alia').on('submit',Show_Alia)
    $('#show_jewel').on('submit',Show_Jewel)
    $(".big_btn").hover(function(){
    $(this).css("background", "#6495ED");
    }, function(){
    $(this).css("background", "white");
  });
});
