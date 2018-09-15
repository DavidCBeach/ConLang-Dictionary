function getRecent() {
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
};


function addWord() {
  let data = $('#add-word-form').serializeArray()
  let word = data[0]['value'];
  let def = data[1]['value'];
  if (!word || !def) {
    alert("Fill out information");
  }
  else {
    $.ajax({
      url: 'http://localhost:8080/$ADD/' + word + '/' + def,
      success: function(result) {
        alert('success');
        getRecent();
      },
      error: function(xhr, status, error) {
        alert("Error fetching recent list.");
      }
    });
  }
}

$(document).ready(function() {
  getRecent();
});
