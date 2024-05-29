from flask import Flask, render_template, request, session, make_response, redirect

app = Flask(__name__)
app.secret_key = "super secret key"

dictionary = {
    "Steve": "Default player",
    "Zombie": "That's a zombie",
    "Creeper": "That guy explodes. Stay away",
    "Enderman": "This guy teleports a lot. He also hits really hard"
}

@app.route('/')
def hello():
    myResponse = make_response(render_template("index.html"))
    myResponse.set_cookie("foo", "bar", max_age=0)
    return myResponse

@app.route('/cookies')
def readCookie():
    return render_template("cookies.html")

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

@app.route('/minecraftdictionary') 
def minecraftDict():
    return render_template("minecraftDictionary.html", dictionary = dictionary)

@app.route('/factorial') 
def factorial():
    return render_template("factorial.html")

@app.route('/factorial/<num>')
def factorialCalc(num):
    fact = 1
    for i in range(1, int(num)+1):
        fact *= i
    return str(fact)

@app.route('/avg')
def average():
    x = int(request.args.get('x'))
    y = int(request.args.get('y'))
    return str((x+y)/2)

@app.route('/login', methods=["post", "get"])
def login():
    message = ''
    if request.method == "POST":
        username = request.form.get("username") 
        password = request.form.get("password") 
        if "username" in session:
            return redirect("/welcome")
        if len(username) <= 5:
            message = "username is too short"
            return render_template("login.html", message=message)
        if username == "AtEchoOff" and password == "asdf":
            message = "Correct username and password"
            session["username"] = username
            return redirect("/welcome")
        else:
            message = "Incorrect username or password"
    if request.method == "GET":
        if "username" in session:
            return redirect("/welcome")

    return render_template("login.html", message=message)

@app.route('/logout')
def logout():
    session.pop('username', None)
    
    return redirect('/login')

@app.route('/welcome')
def welcome():
    if "username" in session:
        return render_template("welcome.html", message="Hello!", username=session['username'])
    else:
        return redirect("/login")
        

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)