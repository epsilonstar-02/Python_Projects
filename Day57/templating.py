from flask import Flask, render_template
import requests

blog_posts = [
    {
        "id": 1,
        "title": "The Art of Python Programming",
        "subtitle": "A Journey into Coding Excellence",
        "body": "Python has become one of the most popular programming languages..."
    },
    {
        "id": 2,
        "title": "Web Development with Flask",
        "subtitle": "Building Modern Web Applications",
        "body": "Flask is a lightweight WSGI web application framework..."
    },
    {
        "id": 3,
        "title": "Data Science Fundamentals",
        "subtitle": "Understanding the Basics",
        "body": "Data science combines multiple fields, including statistics..."
    }
]

app = Flask(__name__)


@app.route('/blog')
def get_blogs():
    return render_template('template1v.html', posts=blog_posts)


@app.route('/guess/<name>')
def main(name):
    gender = requests.get("https://api.genderize.io?", params={'name': name})
    gender = gender.json()['gender'].title()
    age = requests.get("https://api.agify.io?", params={'name': name})
    age = age.json()['age']
    return render_template('template1.html', name=name.title(), gender = gender, age = age)

if __name__ == '__main__':
    app.run(debug=True)