function Verify(){
    $("#results").fadeIn();
    return false;
}

$(document).ready(
  function() {
    $('#quiz_form').on('submit', Verify)
  }
);
