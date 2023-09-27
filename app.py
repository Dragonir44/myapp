from flask import Flask, render_template, request
from Data.users import users
from Function.users_util import get_user_by_id, get_user_by_name
from Function.authors_util import get_author_by_id, get_author_by_name

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/")
def home():
    return render_template("index.html", users=users)

@app.route('/user/<id>')
def user(id):
    user = get_user_by_id(id)
    return render_template("user_details.html", user=user)

@app.route('/author/<id>')
def author(id):
    author = get_user_by_id(id)
    return render_template("author_details.html", author=author)

@app.route('/add', methods=["GET", "POST"])
def addUsers():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("mail")
        age = request.form.get("age")
        bio = request.form.get("bio")
        user_id = len(users)
        new_user = {
            "name": name,
            "email": email,
            "age": age,
            "bio": bio,
            "id": user_id
        }
        
        if get_user_by_name(name):
            return "User already exists"
        else:
            users.append(new_user)
            
            with open(f"myapp/Data/users.py", "w", encoding='utf-8' ) as f:
                f.write(f"users = {users}")
            
            return "User added"
    else:
        return render_template("add.html")