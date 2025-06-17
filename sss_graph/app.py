from flask import Flask, request, jsonify, render_template
from get_table import get_coefficients
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    data = request.json

    family_type = {
        "`Adult(s)`": data["family"].get("adults", 1),
        "`Infant(s)`": data["family"].get("infants", 0),
        "`Preschooler(s)`": data["family"].get("preschoolers", 0),
        "`Schoolager(s)`": data["family"].get("schoolagers", 0),
        "`Teenager(s)`": data["family"].get("teenagers", 0)
    }

    df = get_coefficients(
        data["housing"],
        data["food_plan"],
        **family_type
    )

    return jsonify(df.to_dicts())


if __name__ == '__main__':
    app.run(debug=True)
