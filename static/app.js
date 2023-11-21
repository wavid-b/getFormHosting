function posCheck(that) {
    // hide all elements
    document.getElementById("noun").style.display = "none";
    document.getElementById("verb").style.display = "none";
    document.getElementById("adjective").style.display = "none";

    if (that.value == "noun") {
        // show the noun element
        document.getElementById("noun").style.display = "block";
    } else if (that.value == "verb") {
        document.getElementById("verb").style.display = "block";
    } else if (that.value == "adjective") {
        document.getElementById("adjective").style.display = "block";
    }
}

$(document).ready(function() {
    // Intercept form submission
    $("#lemmatizerForm").submit(function(event) {
      // Prevent default form submission
      event.preventDefault();
  
      // Serialize form data
      var formData = $(this).serialize();
  
      // Make an AJAX request to your Flask route
      $.ajax({
        type: "POST",
        url: "/form", // Replace with the actual route that handles the form submission in your Flask app
        data: formData,
        success: function(response) {
          // Update the content on the page with the received response
          $("#tape").prepend(response.word + ' > ' + response.result + '<br>');
        },
        error: function(error) {
          console.error("Error:", error);
        }
      });
      return false;
    });
  });
  