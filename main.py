from flask import Flask, render_template, request, jsonify
from getForm import get_latin_form
import azure.functions as func
from azure.functions import WsgiMiddleware

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

    # Degree
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
        data = request.form

        wanted_pos = data.get("wanted_pos", "NULL")

        if wanted_pos == "noun":
            result = get_latin_form(
                data.get("wd"),
                case=data.get("case"),
                number=data.get("number"),
                gender=data.get("gender"),
                mood="NULL",
                person="NULL",
                tense="NULL",
                voice="NULL",
                degree="NULL",
                wanted_pos=wanted_pos
            )

            return jsonify({
                "result": result,
                "word": data.get("wd", "").lower(),
                "case": abbreviations.get(data.get("case"), ""),
                "number": abbreviations.get(data.get("number"), ""),
                "gender": abbreviations.get(data.get("gender"), ""),
                "wanted_pos": abbreviations.get(wanted_pos, "")
            })

        elif wanted_pos == "verb":
            result = get_latin_form(
                data.get("wd"),
                case="NULL",
                number=data.get("number"),
                gender="NULL",
                mood=data.get("mood"),
                person=data.get("person"),
                tense=data.get("tense"),
                voice=data.get("voice"),
                degree="NULL",
                wanted_pos=wanted_pos
            )

            return jsonify({
                "result": result,
                "word": data.get("wd", "").lower(),
                "number": abbreviations.get(data.get("number"), ""),
                "mood": abbreviations.get(data.get("mood"), ""),
                "person": abbreviations.get(data.get("person"), ""),
                "tense": abbreviations.get(data.get("tense"), ""),
                "voice": abbreviations.get(data.get("voice"), ""),
                "wanted_pos": abbreviations.get(wanted_pos, "")
            })

        elif wanted_pos == "adjective":
            result = get_latin_form(
                data.get("wd"),
                case=data.get("case"),
                number=data.get("number"),
                gender=data.get("gender"),
                mood="NULL",
                person="NULL",
                tense="NULL",
                voice="NULL",
                degree=data.get("degree"),
                wanted_pos=wanted_pos
            )

            return jsonify({
                "result": result,
                "word": data.get("wd", "").lower(),
                "case": abbreviations.get(data.get("case"), ""),
                "number": abbreviations.get(data.get("number"), ""),
                "gender": abbreviations.get(data.get("gender"), ""),
                "degree": abbreviations.get(data.get("degree"), ""),
                "wanted_pos": abbreviations.get(wanted_pos, "")
            })

    else:
        return render_template("form.html", query="", arrow="", result="")


# -------- AZURE FUNCTIONS ENTRY POINT --------
def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    return WsgiMiddleware(app).handle(req, context)


# -------- LOCAL DEV ONLY --------
if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)