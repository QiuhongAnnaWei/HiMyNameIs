import os
import json
from flask import Flask, request, send_file
from generate import generateOne

app = Flask(__name__, static_url_path='', static_folder='./static',)

@app.route("/")
def home():
  return send_file("./static/index.html")

@app.route('/generate', methods=['GET', 'POST'])
def generateRoute():
    if request.method == "POST":
        print(request) # <Request 'http://localhost:5000/generate' [POST]>
        content = request.json
        print("content", content) #content None
        return json.dumps(generateOne(content['prefix'], content['temperature']))

@app.route("/health")
def healthRoute():
    return "Generate service is up!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
