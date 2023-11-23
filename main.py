from flask import Flask, render_template, request, jsonify
from getForm import get_latin_form, get_greek_form

app = Flask(__name__)

abbreviations = {
    # Part of Speech
    'NULL': '',
    'noun': 'n.',
    'verb': 'v.',
    'adjective': 'adj.',

    # Case
    'nominative': 'nom',
    'genitive': 'gen',
    'dative': 'dat',
    'accusative': 'acc',
    'ablative': 'abl',
    'vocative': 'voc',
    'locative': 'loc',

    # Gender
    'masculine': 'm.',
    'feminine': 'f.',
    'neuter': 'n.',

    # Number
    'singular': 's.',
    'plural': 'pl.',

    # Mood
    'indicative': 'ind',
    'subjunctive': 'subj',
    'infinitive': 'inf',
    'imperative': 'imp',
    'gerund': 'ger',
    'gerundive': 'oblg',

    # Person
    'first': '1st',
    'second': '2nd',
    'third': '3rd',

    # Tense
    'present': 'pres',
    'imperfect': 'imp',
    'perfect': 'perf',
    'pluperfect': 'plup',
    'future perfect': 'fut perf',
    'future': 'fut',

    # Voice
    'active': 'act',
    'passive': 'pass',

    #Degree
    'positive': 'pos',
    'comparative': 'comp',
    'superlative': 'super'
}


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
            return jsonify({"result": result,
                            "word": request.form["wd"].lower(),
                            "case": abbreviations[request.form["case"]],
                            "number": abbreviations[request.form["number"]],
                            "gender": abbreviations[request.form["gender"]],
                            "wanted_pos": abbreviations[request.form["wanted_pos"]]})

            
        elif request.form["wanted_pos"] == "verb": #takes number, mood, person, tense, voice
            result = get_latin_form(request.form["wd"], case = "NULL", number = request.form["number"], gender = "NULL",
                                    mood = request.form["mood"], person = request.form["person"], tense = request.form["tense"],
                                    voice = request.form["voice"], degree = "NULL", wanted_pos = request.form["wanted_pos"])
            return jsonify({
                "result": result,
                "word": request.form["wd"].lower(),
                "number": abbreviations[request.form["number"]],
                "mood": abbreviations[request.form["mood"]],
                "person": abbreviations[request.form["person"]],
                "tense": abbreviations[request.form["tense"]],
                "voice": abbreviations[request.form["voice"]],
                "wanted_pos": abbreviations[request.form["wanted_pos"]]})

        elif request.form["wanted_pos"] == "adjective": #takes gender, number, case, degree
            result = get_latin_form(request.form["wd"], case = request.form["case"], number = request.form["number"], gender = request.form["gender"],
                                    mood = "NULL", person = "NULL", tense = "NULL",
                                    voice = "NULL", degree = request.form["degree"], wanted_pos = request.form["wanted_pos"])
            return jsonify({
                "result": result,
                "word": request.form["wd"].lower(),
                "case": abbreviations[request.form["case"]],
                "number": abbreviations[request.form["number"]],
                "gender": abbreviations[request.form["gender"]],
                "degree": abbreviations[request.form["degree"]],
                "wanted_pos": abbreviations[request.form["wanted_pos"]]})

        """
        elif request.form["wanted_pos"] == "adverb": #takes degree
            result = get_latin_form(request.form["wd"], case = "NULL", number = "NULL", gender = "NULL",
                                    mood = "NULL", person = "NULL", tense = "NULL",
                                    voice = "NULL", degree = request.form["degree"], wanted_pos = request.form["wanted_pos"])
        """
    else:
        return render_template("form.html", query="", arrow="", result="")
    
"""
result = get_latin_form(request.form["wd"], case = request.form["case"], number = request.form["number"], gender = request.form["gender"],
        mood = request.form["mood"], person = request.form["person"], tense = request.form["tense"],
        voice = request.form["voice"], degree = request.form["degree"], wanted_pos = request.form["wanted_pos"])
"""

if __name__ == "__main__":
    app.run(host = "127.0.0.1", port=8000, debug=True)
    