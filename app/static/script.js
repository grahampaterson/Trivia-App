$(document).ready(function() {

  // button function to show all answer
  $('button').click(function() {
    $('.ans').show();
  });

  // report button sends question-id to server
  // and gets back a new question which is appended
  // TODO replace click function with on click function
  $('.report').click(function(){
    $.getJSON('/report', {
      id: $(this).closest('.question-container').attr('id')
    }, function(data) {
      console.log(data)
      $('.page-content').append('<div class="question-container"><div class="que">' + data.newq.q + '</div><div class="ans">' + data.newq.a + '</div><div class="report">report</div></div>')
    });
    $(this).closest('.question-container').fadeOut();
    console.log($(this).closest('.question-container').attr('id'));
  })

  // on clicking a single question show the answer
  $('.que').click(function() {
    $(this).closest('.question-container').find('.ans').toggle();
  })

  // test ajax just makes a request to report page and returns some data that says nothing
  $.getJSON('/report', function(data) {
    console.log(data.nothing);
  });
});
