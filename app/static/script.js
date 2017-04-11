$(document).ready(function() {

  // button function to show all answer
  $('button').click(function() {
    $('.ans').show();
  });

  // report button sends question-id to server
  // and gets back a new question which is appended
  $('.page-content').on('click', '.report', function() {
    $.getJSON('/report', {
      id: $(this).closest('.question-container').attr('id')
    }, function(data) {
      $('button').before(([
        '<div id="' + data.newq.id + '" class="question-container">',
          '<div class="que">' + data.newq.q + '</div>',
          '<div class="ans">' + data.newq.a + '</div>',
          '<div class="report">report</div>',
        '</div>'
      ]).join('\n'))
    });
    $(this).closest('.question-container').fadeOut();
  })

  // on clicking a single question show the answer
  // $('.que').click(function() {
  //   $(this).closest('.question-container').find('.ans').toggle();
  // })

  $('.page-content').on('click', '.que', function() {
    $(this).closest('.question-container').find('.ans').toggle();
  })

  // test ajax just makes a request to report page and returns some data that says nothing
  $.getJSON('/report', function(data) {
    console.log(data.nothing);
  });
});
