from flask import Flask, render_template, url_for, redirect, request
import settings as stg
import db_scripts as db

app = Flask(__name__, static_folder=stg.PATH_STATIC)
app.config['SECRET_KEY'] = stg.SECRET_KEY

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    user = db.getUser()
    print(user)
    return render_template("about.html", user=user)


@app.route("/categories")
def post_categories():
    return render_template("categories.html")


@app.route("/post/category/<category_name>", methods=["GET", "POST"])
def post_category(category_name):
    category_id = db.getIdByCategory(category_name)

    if request.method == "GET":
        posts = db.getPostsByCategory(category_name)
    
    if  request.method == "POST":
        db.addPost(request.form["category_id"], request.form["post"])
        posts = db.getPostsByCategory(category_name)
        return redirect(f"/post/category/{category_name}")

    return render_template("post_category.html", 
                           category_name=category_name,
                           category_id=category_id,
                           posts = posts) 

@app.route("/post/view")
def post_view():
    return "ТУТ БУДЕ МІЙ ПОСТ" 


@app.route("/post/delete/<post_id>/<category_name>")
def deletePost(post_id, category_name):
    db.deletePost(post_id)
    return redirect(f"/post/category/{category_name}")

app.run(debug=True)