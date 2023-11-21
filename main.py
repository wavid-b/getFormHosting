from flask import Flask, render_template, request, jsonify
from getForm import get_latin_form, get_greek_form

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == "POST":

        if request.form["wanted_pos"] == "noun": #takes gender, number, case
            result = get_latin_form(request.form["wd"], case = request.form["case"], number = request.form["number"], gender = request.form["gender"],
                                    mood = "NULL", person = "NULL", tense = "NULL",
                                    voice = "NULL", degree = "NULL",  wanted_pos = request.form["wanted_pos"])
            
        elif request.form["wanted_pos"] == "verb": #takes number, mood, person, tense, voice
            result = get_latin_form(request.form["wd"], case = "NULL", number = request.form["number"], gender = "NULL",
                                    mood = request.form["mood"], person = request.form["person"], tense = request.form["tense"],
                                    voice = request.form["voice"], degree = "NULL", wanted_pos = request.form["wanted_pos"])
            
        elif request.form["wanted_pos"] == "adjective": #takes gender, number, case, degree
            result = get_latin_form(request.form["wd"], case = request.form["case"], number = request.form["number"], gender = request.form["gender"],
                                    mood = "NULL", person = "NULL", tense = "NULL",
                                    voice = "NULL", degree = request.form["degree"], wanted_pos = request.form["wanted_pos"])

        """
        elif request.form["wanted_pos"] == "adverb": #takes degree
            result = get_latin_form(request.form["wd"], case = "NULL", number = "NULL", gender = "NULL",
                                    mood = "NULL", person = "NULL", tense = "NULL",
                                    voice = "NULL", degree = request.form["degree"], wanted_pos = request.form["wanted_pos"])
        """

        return jsonify({"result": result,
                        "word": request.form["wd"]})
    else:
        return render_template("form.html", query="", arrow="", result="")
    
"""
result = get_latin_form(request.form["wd"], case = request.form["case"], number = request.form["number"], gender = request.form["gender"],
        mood = request.form["mood"], person = request.form["person"], tense = request.form["tense"],
        voice = request.form["voice"], degree = request.form["degree"], wanted_pos = request.form["wanted_pos"])
"""

if __name__ == "__main__":
    app.run(host = "10.0.0.102", port=8000, debug=True)