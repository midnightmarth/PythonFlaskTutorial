from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/credits')
def credits():
    return render_template("credits.html")

@app.route('/vars/<num>')
def vars(num):
    output = f"You chose number {int(num)} which is 1 more than {int(num) - 1}"
    output += "<br> <a href='/'>Home</a>"
    return output



if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)