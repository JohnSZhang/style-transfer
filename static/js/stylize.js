$(function() {

  // $("#input input, #input textarea").jqBootstrapValidation({
  //   preventSubmit: true,
  //   submitError: function($form, event, errors) {
  //     // additional error messages or events
  //   },
  //   submitSuccess: function($form, event) {
  //     event.preventDefault(); // prevent default submit behaviour
  //     // get values from FORM
  //     var message = $("textarea#message").val();
  //     $this = $("#sendMessageButton");
  //     $this.prop("disabled", true); // Disable submit button until AJAX call is complete to prevent duplicate messages
  //     $.ajax({
  //       url: "./inference",
  //       type: "POST",
  //       data: {
  //         text: message
  //       },
  //       cache: false,
  //       success: function(output) {
  //         $('#output').text(output);
  //         // Success message
  //         $('#success > .alert-success')
  //           .append("<strong>Your message has been sent. </strong>");
  //       },
  //       error: function() {
  //         // Fail message
  //         $('#success').html("<div class='alert alert-danger'>");
  //         $('#success > .alert-danger').html("<button type='button' class='close' data-dismiss='alert' aria-hidden='true'>&times;")
  //           .append("</button>");
  //         $('#success > .alert-danger').append($("<strong>").text("Sorry it seems that stylize server is not responding. Please try again later!"));
  //         $('#success > .alert-danger').append('</div>');
  //         //clear all fields
  //         $('#contactForm').trigger("reset");
  //       },
  //       complete: function() {
  //         setTimeout(function() {
  //           $this.prop("disabled", false); // Re-enable submit button when AJAX call is complete
  //         }, 1000);
  //       }
  //     });
  //   },
  //   filter: function() {
  //     return $(this).is(":visible");
  //   },
  // });
  //
  // $("a[data-toggle=\"tab\"]").click(function(e) {
  //   e.preventDefault();
  //   $(this).tab("show");
  // });

    var waiting_resp = false;

    $("#user-text").bind('input propertychange', function () {
        var s_end = ['.', '!', '?'];
        var user_text = $('#user-text')[0].value.trim();

        var sentence_end = false;
        var last_char = user_text[user_text.length - 1];
        for (var i=0; i < s_end.length; i++) {
            if (s_end[i] == last_char) {
                sentence_end = true;
            }
        }

        if (sentence_end) {
            $.ajax({
                url: "./inference",
                type: "POST",
                data: {
                    text: user_text
                },
                success: function (output) {
                    $('#style-transfer').text(output);
                }
            });
        } else if (!waiting_resp) {
            waiting_resp = true;
            $.ajax({
                url: "./complete",
                type: "POST",
                data: {
                    text: user_text
                },
                success: function (output) {
                    $('#completion').text(output);
                    waiting_resp = false;
                }
            });
        }
    });


    $("#copy-complete").on('click', function () {
        $('#user-text')[0].value = $('#completion').text();
    });

    $("#copy-style").on('click', function () {
        $('#user-text')[0].value = $('#style-transfer').text();
    });

    $("#add-to").on('click', function () {
        var to_add = $('#user-text')[0].value.trim();
        $('#user-text')[0].value = "";
        var so_far = $('#output')[0].value;
        $('#output')[0].value = so_far + to_add;
        $('#user-text')[0].focus();
    });

});

