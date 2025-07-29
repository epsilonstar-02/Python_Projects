from flask import Flask, render_template, request
import datetime
app = Flask(__name__)

@app.route('/')
def main():
    year = datetime.date.today().year
    name = input("What is your name? ")
    return render_template('index.html', year=year, name=name)

if __name__ == '__main__':
    app.run(debug=True)