from flask import Flask, render_template, request, session, make_response, redirect, jsonify
import mysql.connector

app = Flask(__name__)
app.secret_key = "super secret key"

myDatabase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="halolord8",
    database="sql_store"
)

mycursor = myDatabase.cursor()

dictionary = {
    "Steve": "Default player",
    "Zombie": "That's a zombie",
    "Creeper": "That guy explodes. Stay away",
    "Enderman": "This guy teleports a lot. He also hits really hard"
}

friendsList = ["Steve", "Clara", "Exavieer", "Evelyn"]

links = {
    "Home": "/",
    "Factorial": "/factorial",
    "Minecraft Dictionary": "/minecraftdictionary",
    "Cookies": "/cookies",
    "Login": "/login",
    "About": "/about",
    "Credits": "/credits",
    "People" : "/people",   
    "Friends": "/friends"
}

@app.route('/')
def index():
    return render_template("index.html", links=links)

@app.route('/cookies', methods = ["get", "post"])
def readCookie():
    if request.method == "GET":
        response = make_response(render_template("cookies.html", links=links))
        response.set_cookie("userID", "someUser", max_age=60*60*24*365)
        return response
    elif request.method == "POST":
        response = make_response(render_template("cookies.html", links=links))
        response.set_cookie("userID", request.form.get("cookieVal"), max_age=60*60*24*365)
        return response

@app.route('/delcookie', methods = ["get"])
def delCookie():
    response = make_response(render_template("cookies.html", links=links))
    response.delete_cookie("userID")
    return response

@app.route('/about')
def about():
    return render_template("about.html", links=links)

@app.route('/credits')
def credits():
    return render_template("credits.html", links=links)

@app.route('/vars/<num>') 
def vars(num):
    return f"<div id='someIdThatDoesntWork'>You chose number {int(num)} which is 1 more than {int(num) - 1} <br> <a href='/'>Home</a></div>"

@app.route('/minecraftdictionary') 
def minecraftDict():
    return render_template("minecraftDictionary.html", dictionary=dictionary, links=links)

@app.route('/factorial') 
def factorial():
    return render_template("factorial.html", links=links)

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
            return render_template("login.html", message=message, links=links)
        if username == "AtEchoOff" and password == "asdf":
            session["username"] = username
            response = make_response(render_template('welcome.html', links=links))
            return response
        else:
            message = "Incorrect username or password"
    if request.method == "GET":
        if "username" in session:
            return redirect("/welcome")

    return render_template("login.html", message=message, links=links)

@app.route('/logout')
def logout():
    session.pop('username', None)
    
    return redirect('/login')

@app.route('/welcome')
def welcome():
    if "username" in session:
        return render_template("welcome.html", message="Hello!", username=session['username'], links=links)
    else:
        return redirect("/login")
        
@app.route('/people', methods=["get", "post"])
def people():
    if request.method == "GET":
        mycursor.execute("SELECT first_name, last_name, birth_date FROM customers")
        list = mycursor.fetchall()
        return render_template("people.html", people=list, links=links)
    elif request.method == "POST":
        list = []
        firstName = request.form.get("firstName")
        lastName = request.form.get("lastName")
        age = request.form.get("age")
        mycursor.execute(f"INSERT INTO customers VALUES(%s, %s, %s)", [firstName, lastName, age])
        myDatabase.commit()
        mycursor.execute("SELECT * FROM people")
        list = mycursor.fetchall()
        return render_template("people.html", people=list, links=links)





@app.route('/friends', methods=['GET'])
def friends():
    return render_template("friends.html", links=links)


@app.route('/api/friends/all', methods=['GET'])
def api_all():
    return jsonify(friendsList)

@app.route('/api/friends', methods=['GET', 'POST'])
def api_one():
    if request.method == 'POST':
        newFriend = request.get_json()
        friendsList.append(newFriend)
        return jsonify(friendsList)

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT, debug=True)