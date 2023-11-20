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