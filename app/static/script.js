$(document).ready(function() {
  $('button').click(function() {
    $('.ans').toggle();
  });

  console.log("working")

  $('a').click(function(){
    $.getJSON('/ajax_test', {
      id: $(this).closest('.question-container').attr('id')
    }, function() {

    });
    $(this).parent().append('<span>reported</span>');
    $(this).hide();
    console.log($(this).closest('.question-container').attr('id'))
  })

  $.getJSON('/ajax_test', function(data) {
    console.log(data.something);
  });
});
