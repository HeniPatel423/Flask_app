from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def get_student_number():
    # Return student number in JSON format
    student_number = {"student_number": "200544300"}
    return jsonify(student_number)

@app.route('/webhook')
def get_webhook_response():
    # Return text for Dialogflow integration
    return "Text for Dialogflow integration"

if __name__ == '__main__':
    app.run(debug=True)