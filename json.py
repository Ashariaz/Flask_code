from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/greet/<name>', methods=['GET'])
def greet(name):
    greeting = f"Hello, {name}!"
    data = {
        'message': greeting
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

