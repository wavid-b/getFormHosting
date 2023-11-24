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
    var tapeLine = `${response.word} (${response.wanted_pos})`
    if (response.wanted_pos == "n." || response.wanted_pos == "adj.") {
        if (response.gender.length > 0) {
            tapeLine += ` + ${response.gender}`
        }
        if (response.number.length > 0) {
            tapeLine += ` + ${response.number}`
        }
        if (response.case.length > 0) {
            tapeLine += ` + ${response.case}`
        }
        if (response.degree && response.degree.length > 0) {
            tapeLine += ` + ${response.degree}`;
        }
        return tapeLine += ` => ${response.result}`
        //return (response.word + ' (' + response.wanted_pos + ')' + " + " + response.gender + " + " + response.number + " + " + response.case + " => " + response.result);
    }
    if (response.wanted_pos == "v.") {
        if (response.wanted_pos == "v.") {
            if (response.person.length > 0) {
                tapeLine += ` + ${response.person}`;
            }
            if (response.number.length > 0) {
                tapeLine += ` + ${response.number}`;
            }
            if (response.tense.length > 0) {
                tapeLine += ` + ${response.tense}`;
            }
            if (response.voice.length > 0) {
                tapeLine += ` + ${response.voice}`;
            }
            if (response.mood.length > 0) {
                tapeLine += ` + ${response.mood}`;
            }
            return tapeLine += ` => ${response.result}`;
        }
    }
  }

$(document).ready(function() {
    var html = document.getElementsByTagName('html');
    var radios = document.getElementsByName('wanted_pos');

    for (i = 0; i < radios.length; i++) {
        radios[i].addEventListener('change', function() {
            posCheck(this);});
    }

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

