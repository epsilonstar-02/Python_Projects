from flask import Flask, render_template
import requests

app = Flask(__name__)

# Fetch blog posts from an external API
def get_blog_posts():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return all_posts

@app.route('/')
def home():
    all_posts = get_blog_posts()
    return render_template("index.html", posts=all_posts)

@app.route("/post/<int:index>")
def show_post(index):
    all_posts = get_blog_posts()
    requested_post = None
    for blog_post in all_posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
