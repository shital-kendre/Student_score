from flask import Flask, request, render_template, jsonify
from utils import get_s_score

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_score', methods = ['POST'])
def get_student_predicted_price():
    data = request.form

    pred_score = get_s_score(data)
    print("Predicted price is:", pred_score )

    return jsonify({"Predicted student score": pred_score})

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5080)