from flask import Flask, request\napp = Flask(__name__)\n\n@app.route('/')\ndef index():\n    return 'TP Proactif - OK'\n\nif __name__ == '__main__':\n    app.run(host='0.0.0.0', port=5000)\n
