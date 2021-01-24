import os
import json
from flask import Flask, request
from generate import generateOne

app = Flask(__name__)

@app.route("/generate")
def generateRoute():
    return "backend"
    # return json.dumps(generateOne(request.args.get('prefix')))

@app.route("/health")
def healthRoute():
    return "Generate service is up!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
