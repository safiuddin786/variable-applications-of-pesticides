from flask import Flask, request, jsonify

from modeltest import predictModel
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/predict', methods=['GET'])
def predict():
    image = request.args.get('image')
    result = ""
    if request.method == 'GET':
        print("hell")
        result = predictModel(image)
    return result

if __name__ == '__main__':
	app.run(host="0.0.0.0",)