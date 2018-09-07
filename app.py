from flask import Flask, render_template
import definitions as df

app = Flask(__name__)

@app.route('/')
def main():
    df.init()
    return render_template('main.html', recent=recent)

# Run server on localhost
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
