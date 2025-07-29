from flask import Flask, render_template, url_for
import requests
import json
from post import Post

blogs = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
blog = [Post(post['id'], post['title'],post['subtitle'], post['body']) for post in blogs.json()]
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts=blogs.json())

@app.route('/post/<int:post_id>')
def post(post_id):
    for post in blog:
        if post.post_id == post_id:
            return render_template('post.html', title=post.title, subtitle=post.subtitle, body=post.content)


if __name__ == "__main__":
    app.run(debug=True)
