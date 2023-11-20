from flask import Flask, render_template, request
from getForm import get_latin_form, get_greek_form

app = Flask(__name__)

"""
@app.route('/', methods=['GET', 'POST'])
def home():
    return get_latin_form("mater", gender = "f", number = "p", case = "a")
"""
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == "POST":
        return get_latin_form(request.form["wd"], case = request.form["case"], number = request.form["number"], gender = request.form["gender"],
                              mood = request.form["mood"], person = request.form["person"], tense = request.form["tense"],
                              voice = request.form["voice"], degree = request.form["degree"], wanted_pos = request.form["wanted_pos"])
    else:
        return render_template("form.html")

if __name__ == "__main__":
    app.run(port=8000, debug=True)