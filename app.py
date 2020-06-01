from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def test():
    return jsonify({'message':'Test API GET'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
