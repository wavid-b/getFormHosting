function posCheck(that) {
    // hide all
    const noun = document.getElementsByClassName("noun");
    for (let i = 0; i < noun.length; i++) {
        noun[i].style.display = "none";
    }
    const verb = document.getElementsByClassName("verb");
    for (let i = 0; i < verb.length; i++) {
        verb[i].style.display = "none";
    }
    const adjective = document.getElementsByClassName("adjective");
    for (let i = 0; i < adjective.length; i++) {
        adjective[i].style.display = "none";
    }

    if (that.value == "noun") {
        for (let i = 0; i < noun.length; i++) {
            noun[i].style.display = "block";
        }
    } else if (that.value == "verb") {
        for (let i = 0; i < verb.length; i++) {
            verb[i].style.display = "block";
        }
    } else if (that.value == "adjective") {
        for (let i = 0; i < adjective.length; i++) {
            adjective[i].style.display = "block";
        }
    }
}

function makeTapeLine(response) {
    if (response.wanted_pos == "n.") {
        return (response.word + ' (' + response.wanted_pos + ')' + " + " + response.gender + " + " + response.number + " + " + response.case + " => " + response.result);
    }
    if (response.wanted_pos == "v.") {
        return (response.word + ' (' + response.wanted_pos + ')' + " + " + response.person + " + " + response.number + " + " + response.tense + " + " + response.voice + " + " + response.mood + " => " + response.result);
    }
    if (response.wanted_pos == "adj.") {
        return (response.word + ' (' + response.wanted_pos + ')' + " + " + response.gender + " + " + response.number + " + " + response.case + " => " + response.result);
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
        url: "/form",
        data: formData,
        success: function(response) {
            alert(response.wanted_pos)
            // Update the content on the page with the received response
            $("#tapeTitle").html('<h4>History:</h4>');
            let tapeLine = makeTapeLine(response);
            $("#tape").prepend(tapeLine + '<br>');
        },
        error: function(error) {
          console.error("Error:", error);
        }
      });
      return false;
    });
  });

