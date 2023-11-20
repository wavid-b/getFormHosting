from flask import Flask, render_template, request
from getForm import get_latin_form, get_greek_form

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == "POST":
        result = get_latin_form(request.form["wd"], case = request.form["case"], number = request.form["number"], gender = request.form["gender"],
                              mood = request.form["mood"], person = request.form["person"], tense = request.form["tense"],
                              voice = request.form["voice"], degree = request.form["degree"], wanted_pos = request.form["wanted_pos"])
        return render_template("form.html", result = result)
    else:
        return render_template("form.html", result = "")

if __name__ == "__main__":
    app.run(port=8000, debug=True)