from flask import Flask, render_template, jsonify
import definitions as df
import sys

app = Flask(__name__)


@app.route('/')
def main():
    df.init()
    return render_template('main.html')


######### API ROUTES #########
@app.route('/$RECENT')
@app.route('/$RECENT/')
def recent():
    recent = df.recent()
    return jsonify(recent)


@app.route('/$ADD/<string:word>/<string:definition>')
@app.route('/$ADD/<string:word>/<string:definition>/')
def addword(word, definition):
    if (df.addWord(word, definition)):
        return "", 200
    else:
        return "", 500

# Run server on localhost
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
