from flask import Flask, jsonify, request
app = Flask(__name__)

language = [{'name' : 'Python'}, {'name' : 'FLask'}, {'name' : 'Django'}, {'name' : 'C++'}]

@app.route('/', methods=['GET'])
def test():
    return jsonify({'message':'Test API GET'})

@app.route('/lang', methods={'GET'})
def returnAll():
    return jsonify({'language' : language})

@app.route('/lang/<string:name>', methods=['GET'])
def returnOnly(name):
    langs = [language for language in language if language['name'] == name]
    return jsonify({'language' : langs[0]})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
