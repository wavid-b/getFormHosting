import flask as fl
from getForm import get_latin_form, get_greek_form

app = fl.Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return get_latin_form("mater", gender = "f", number = "p", case = "a")

if __name__ == "__main__":
    app.run(port=8000, debug=True)