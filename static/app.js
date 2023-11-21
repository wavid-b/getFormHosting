function posCheck(that) {
    // hide all elements
    document.getElementsByClassName("noun")[0].style.display = "none";
    document.getElementsByClassName("verb")[0].style.display = "none";
    document.getElementsByClassName("adjective")[0].style.display = "none";

    if (that.value == "noun") {
        // show the noun element
        document.getElementsByClassName("noun")[0].style.display = "block";
    } else if (that.value == "verb") {
        document.getElementsByClassName("verb")[0].style.display = "block";
    } else if (that.value == "adjective") {
        document.getElementsByClassName("adjective")[0].style.display = "block";
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
          $("#tapeTitle").html('<h4>History:</h4>');
          $("#tape").prepend(response.word + ' > ' + response.result + '<br>');
        },
        error: function(error) {
          console.error("Error:", error);
        }
      });
      return false;
    });
  });
  