from fastapi import FastAPI
from flask import Flask, request, jsonify, render_template,jsonify
import util
from fastapi.middleware.wsgi import WSGIMiddleware

app = Flask(__name__)
App = FastAPI()
App.mount("/", WSGIMiddleware(app))

util.load_saved_artifacts()
@app.route('/classify_image', methods=['GET', 'POST'])
def classify_image():
    image_data = request.form['image_data']
    response = jsonify(util.classify_image(image_data))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        return jsonify("Sucesss")
if __name__ == "__main__":
    print("Starting Python Flask Server For Sports Celebrity Image Classification")
    
