(function() {
  $.ajax({
    url: 'http://localhost:8080/$RECENT',
    success: function(result) {
      for (i in result) {
        $('#recent').append("<li>" + result[i] + "</li>")
      }
    },
    error: function(xhr, status, error) {
      console.log("Error fetching recent list.");
    }
  });
})();
