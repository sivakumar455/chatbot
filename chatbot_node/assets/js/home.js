(function (window, $) {
  const Home = function() {
    const oThis = this;

    oThis.bindEvents();
    oThis.query = null;
  };

  Home.prototype = {
    bindEvents: function() {
      const oThis = this;

      $('button#send-btn').click(function(event) {
        event.preventDefault();

        var data = $('#query-form').serializeArray();

        oThis.query = data;

        var html = '<p class="query-input">' + data[0].value + '</p>';
        $(".messages").append(html);

        var successCallback = function(resp) {
          var html = '<p class="query-output">' + resp.predicted + '</p>';
          $(".messages").append(html);
        };
 
        oThis.callApi(successCallback);

        $('.messages').animate({
          scrollTop: $(".messages p:last-child").position().top
        }, "fast");

        $('input[name=q').val('');
        oThis.query = null;
      });
    },

    callApi: function(successCallback) {
      const oThis = this;

      $.ajax({
        url: 'http://192.168.1.6:5000/go',
        type: 'GET',
        data: oThis.query,
        contentType: 'application/json',
        success: function(response) {
          successCallback(response);
        },
        error: function(error) {
          console.error('===error', error);
        }
      });
    }
  };

  window.Home = Home;
})(window, jQuery); 