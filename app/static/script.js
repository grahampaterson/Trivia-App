$(document).ready(function() {

  // button function to show all answer
  $('button').click(function() {
    $('.ans').show();
  });

  // report button sends question-id to server
  $('.report').click(function(){
    $.getJSON('/ajax_test', {
      id: $(this).closest('.question-container').attr('id')
    }, function() {

    });
    $(this).parent().append('<div>reported</div>');
    $(this).hide();
    console.log($(this).closest('.question-container').attr('id'));
  })

  // on clicking a single question show the answer
  $('.que').click(function() {
    $(this).closest('.question-container').find('.ans').toggle();
  })

  // test ajax just makes a request to ajax test page and returns some data
  $.getJSON('/ajax_test', function(data) {
    console.log(data.something);
  });
});
