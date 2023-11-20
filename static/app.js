function posCheck(that) {
    if (that.value == "noun") {
        document.getElementById("noun").style.display = "block";
        // hide all others
        document.getElementById("verb").style.display = "none";
        document.getElementById("adverb").style.display = "none";
        document.getElementById("adjective").style.display = "none";

    } else if (that.value == "verb") {
        document.getElementById("verb").style.display = "block";
        // hide all others
        document.getElementById("noun").style.display = "none";
        document.getElementById("adverb").style.display = "none";
        document.getElementById("adjective").style.display = "none";

    } else if (that.value == "adverb") {
        document.getElementById("adverb").style.display = "block";
        // hide all others
        document.getElementById("noun").style.display = "none";
        document.getElementById("verb").style.display = "none";
        document.getElementById("adjective").style.display = "none";

    } else if (that.value == "adjective") {
        document.getElementById("adjective").style.display = "block";
        // hide all others
        document.getElementById("noun").style.display = "none";
        document.getElementById("verb").style.display = "none";
        document.getElementById("adverb").style.display = "none";
    } else {
        // hide all
        document.getElementById("noun").style.display = "none";
        document.getElementById("verb").style.display = "none";
        document.getElementById("adverb").style.display = "none";
        document.getElementById("adjective").style.display = "none";
    }
}